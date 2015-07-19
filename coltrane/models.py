import datetime
from django.conf import settings
from django.db import models
from markdown import markdown
from django.contrib.auth.models import User
from tagging.fields import TagField, Tag
import tagging
#from tagging.registry import register
from django.core.urlresolvers import reverse
import pytz
from django.utils import timezone

from dbgp.client import brk


class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()        

    class Meta: 
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title
    
    #def get_absolute_url(self):
    #    return "/categories/%s/" % self.slug
    def get_absolute_url(self):
        #return "/weblog/categories/%s/" % self.slug
        #return reverse('coltrane_category_detail', (), kwargs = {'slug': self.slug})
        return reverse('coltrane_category_detail', kwargs = {'slug':self.slug})

class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    # Core fields.
    title = models.CharField(max_length=250,help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True,help_text="A short summary of the Entry, Optional." )
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)


    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date')
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TagField()

    # Need to be this way around so that non-live entries will show up in Admin, which uses the default (first) manager.
    objects = models.Manager()
    live = LiveEntryManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
    
    
    def get_absolute_url(self):
        date_string = self.pub_date.strftime("%Y/%b/%d").lower()
        #brk(host="localhost",port=53891)
        #return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(),self.slug)
        return reverse('coltrane_entry_detail', kwargs = {'year': self.pub_date.strftime("%Y"), 'month':self.pub_date.strftime("%b"), 'day':self.pub_date.strftime("%d"),'slug':self.slug})


# See http://blog.sveri.de/index.php?/categories/2-Django
tagging.register(Entry, tag_descriptor_attr='etags')


class Link(models.Model):
    # Metadata.
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to Delicious', default=True, help_text='If checked, this will be posted both to your weblog and to your delicious.com account. (Currently disabled)')
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date', help_text='Must be unique for the publication date.')
    title = models.CharField(max_length=250)
    
    # The actual link bits.
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False, blank=True)
    via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')
    url = models.URLField('URL', unique=True)
    tags = TagField()
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
    
    def save(self):
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER, 
                            settings.DELICIOUS_PASSWORD, 
                            smart_str(self.url), 
                            smart_str(self.title), 
                            smart_str(self.tags))
        if self.description:
            self.description_html = markdown(self.description)
        super(Link, self).save()
    
    def get_absolute_url(self): 
        return reverse('coltrane_link_detail', kwargs = {'year': self.pub_date.strftime("%Y"), 'month':self.pub_date.strftime("%m"), 'day':self.pub_date.strftime("%d"),'slug':self.slug})

# See http://blog.sveri.de/index.php?/categories/2-Django
tagging.register(Link, tag_descriptor_attr='etags')


from akismet import Akismet
from django.conf import settings
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_will_be_posted
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str
from django.core.mail import mail_managers

def moderate_comment(sender, comment, request, **kwargs): 
     if not comment.id:
         brk(host="localhost",port=53891)
         mail_managers("New comment posted", email_body % (comment.name, comment.content_object))

         entry = comment.content_object
         delta = datetime.datetime.now(timezone.utc) - entry.pub_date
         if delta.days > 30:
             comment.is_public = False
         else:
             akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url="http:/%s/" %Site.objects.get_current().domain)
             if akismet_api.verify_key():
                 akismet_data = { 'comment_type': 'comment',
                                  'referrer': request.META['HTTP_REFERER'],
                                  'user_ip': comment.ip_address,
                                  'user-agent': request.META['HTTP_USER_AGENT'] }
                 if akismet_api.comment_check(smart_str(comment.comment),
                                             akismet_data,
                                             build_data=True):
                     comment.is_public = False
         email_body = "%s posted a new comment on the entry '%s'."
         mail_managers("New comment posted", email_body % (comment.name, comment.content_object))
                     
comment_will_be_posted.connect(moderate_comment, sender=Comment)

from django.db import models
from annuaire.models import Student


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.title)


class SubCategory(models.Model):
    c_id = models.ForeignKey(Category)
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.title)


class Thread(models.Model):
    sc_id = models.ForeignKey(SubCategory)
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(Student)

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return self.post_set.count() - 1


class Post(models.Model):
    creator = models.ForeignKey(Student)
    created = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=100000)

    def __unicode__(self):
        return u"%s" % self.thread


class Comment(models.Model):
    creator = models.ForeignKey(Student)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return u"%s" % self.post

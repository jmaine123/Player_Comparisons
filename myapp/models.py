# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Boxscore(models.Model):
    loser = models.TextField(db_column='Loser', blank=True, null=True)  # Field name made lowercase.
    loserscore = models.IntegerField(db_column='LoserScore', blank=True, null=True)  # Field name made lowercase.
    winner = models.TextField(db_column='Winner', blank=True, null=True)  # Field name made lowercase.
    winnerscore = models.IntegerField(db_column='WinnerScore', blank=True, null=True)  # Field name made lowercase.
    topscorer = models.TextField(db_column='TopScorer', blank=True, null=True)  # Field name made lowercase.
    topscorerpoints = models.IntegerField(db_column='TopScorerPoints', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxScore'


class Playersinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    player_id = models.TextField(db_column='Player_id', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    position = models.TextField(db_column='Position', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.TextField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    college = models.TextField(db_column='College', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playersInfo'


class Debate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p1_id = models.IntegerField(default=0)
    p2_id = models.IntegerField(default=0)
    p1_name = models.TextField(blank=True, null=True)
    p2_name = models.TextField(blank=True, null=True)
    p1_user_id = models.TextField(blank=True, null=True)
    p2_user_id = models.TextField(blank=True, null=True)
    p1_vote = models.IntegerField(default=0)
    p2_vote = models.IntegerField(default=0)
    user_pick = models.TextField(default='1')

    class Meta:
        managed = True
        db_table = 'debate'


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        db_table ='follower'

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)

class DebateStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    open_debate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    opinion_total = models.IntegerField(default=0)


    class Meta:
        db_table = 'debateStatus'

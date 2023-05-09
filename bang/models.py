from django.db import models

# Create your models here.

class Member(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    nname = models.CharField(max_length=20, primary_key=True)
    rdate = models.DateTimeField()
    def __str__(self):
        return self.nname

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    nname = models.CharField(max_length=20)
    rdate =  models.DateTimeField()
    lookup = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    ccode = models.CharField(max_length=20)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class  Comment(models.Model):
    board = models.ForeignKey(Board, related_name='board_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment

class Vote(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    voter = models.CharField(max_length=20)
    def __str__(self):
        return self.voter

class Champion(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    nname = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    loc  = models.CharField(max_length=30)
    health = models.CharField(max_length=30)
    recover = models.CharField(max_length=30)
    attack = models.CharField(max_length=30)
    defence = models.CharField(max_length=30)
    resist = models.CharField(max_length=30)
    aspeed = models.CharField(max_length=30)
    mspeed = models.CharField(max_length=30)
    image = models.ImageField()
    bigimage = models.ImageField()
    def __str__(self):
        return self.name
    #,",",self.nname,",",self.role,",",self.loc,",",self.health,",",self.recover,",",self.attack,",",self.defence,",",self.resist,",",self.aspeed,",",self.mspeed

class Skill(models.Model):
    name = models.ForeignKey(Champion, on_delete=models.CASCADE)
    skill_q  = models.CharField(max_length=30)
    skill_w = models.CharField(max_length=30)
    skill_e = models.CharField(max_length=30)
    skill_r = models.CharField(max_length=30)
    skill_p = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Rune(models.Model):
    rname = models.CharField(max_length=30, primary_key=True)
    build = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    def __str__(self):
        return self.rname

class Video(models.Model):
    link = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    runtime = models.CharField(max_length=15)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.link
from django.db import models
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, ManyToManyWidget


class Authors(models.Model):
    Author = models.CharField(max_length=255, verbose_name="Author's Name", blank=True, null=True)
    Petitions = models.ManyToManyField('Texts', blank=True)
    Author_prefecture = models.CharField(max_length=255, blank=True, null=True)
    Birth_year = models.CharField(max_length=255, blank=True, null=True)
    Death_year = models.CharField(max_length=255, blank=True, null=True)
    Details = models.TextField(blank=True, null=True)
    Office = models.CharField(max_length=255, blank=True, null=True)
    Other_names = models.CharField(max_length=255, blank=True, null=True)
    Rank = models.CharField(max_length=255, blank=True, null=True)
    Romanized_name = models.CharField(max_length=255, blank=True, null=True)
    Sources = models.TextField(blank=True, null=True)
    Status = models.TextField(blank=True, null=True)
    urls = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Authors'
    def __unicode__(self):
        return u"%s" % (self.Author)


#class Kenpakusho(models.Model):
#petitions
#    Petition_number = models.CharField(max_length=255, blank=True, null=True)
#    Author = models.ManyToManyField(Authors, blank=True)
#    Title = models.CharField(max_length=255, blank=True, null=True)	
#    Year = models.CharField(max_length=255, blank=True, null=True)	
#    Date_in_Japanese = models.CharField(max_length=255, blank=True, null=True)		
#    Clean_text = models.TextField(blank=True, null=True)	
#    Original_or_copy = models.CharField(max_length=255, blank=True, null=True)	
#    Paper_type = models.CharField(max_length=255, blank=True, null=True)	
#    Prefecture = models.CharField(max_length=255, blank=True, null=True)	
#    Detailed_location = models.CharField(max_length=255, blank=True, null=True)		
#    Author_position = models.CharField(max_length=255, blank=True, null=True)	
#    Author = models.CharField(max_length=255, blank=True, null=True)	
#    Addressee = models.CharField(max_length=255, blank=True, null=True)	
#    Archive = models.CharField(max_length=255, blank=True, null=True)	
#    Count = models.CharField(max_length=255, blank=True, null=True)	



class Texts(models.Model):
#repetition of data from petitions
    Sort_key = models.CharField(max_length=255, blank=True, null=True)	
    Authors = models.ManyToManyField('Authors', blank=True)
    Title = models.CharField(max_length=255, blank=True, null=True)	
    Clean_text = models.TextField(blank=True, null=True)	
    Year = models.CharField(max_length=255, blank=True, null=True)	
    Month = models.CharField(max_length=255, blank=True, null=True)	
    Day = models.CharField(max_length=255, blank=True, null=True)		
    Number_in_arabic_numbers = models.CharField(max_length=255, blank=True, null=True)
    Petition_number = models.CharField(max_length=255, blank=True, null=True)
    Original_or_copy = models.CharField(max_length=255, blank=True, null=True)	
    Date_in_Japanese = models.CharField(max_length=255, blank=True, null=True)		
    Paper_type = models.CharField(max_length=255, blank=True, null=True)	
    Prefecture = models.CharField(max_length=255, blank=True, null=True, choices=(('1', '1'),('2','2')))	
    Detailed_location = models.CharField(max_length=255, blank=True, null=True)		
    Temp_residence = models.CharField(max_length=255, blank=True, null=True, choices=(('1', '1'),('2','2')))	
    Author_position = models.CharField(max_length=255, blank=True, null=True)	
    Author = models.CharField(max_length=255, blank=True, null=True)	
    Addressee = models.CharField(max_length=255, blank=True, null=True)	
    Archive = models.CharField(max_length=255, blank=True, null=True)	
    Date_unclear = models.BooleanField(blank=True)		
    Title_source =  models.CharField(max_length=255, blank=True, null=True, choices=(('From text', 'From text'),('Assigned by editors','Assigned by editors'),('Assigned by institution','Assigned by institution')))	
    Ravina_checked = models.BooleanField(blank=True)	
    Armstrong_checked = models.BooleanField(blank=True)	
    Corrections = models.TextField(blank=True, null=True)	
    Last_action = models.CharField(max_length=255, blank=True, null=True)	
    Number_finder = models.CharField(max_length=255, blank=True, null=True)	
    Genro = models.CharField(max_length=255, blank=True, null=True)	
    Glitch = models.CharField(max_length=255, blank=True, null=True)	
    Full_text_with_CR = models.TextField(blank=True, null=True)		
    NEWLINE = models.CharField(max_length=255, blank=True, null=True)	
    Processing = models.TextField(blank=True, null=True)	
#    Authors::Author	
#    Authors::Author_ID	
#    Authors::Author_prefecture	
    Count = models.CharField(max_length=255, blank=True, null=True)	

    class Meta:
        verbose_name = 'Texts'
        verbose_name_plural = 'Texts'
    def __unicode__(self):
        return u"%s" % (self.Sort_key)


#class Key(models.Model):
#linking between Petition_number and Author
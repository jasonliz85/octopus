from django.db import models
from .encryption import *

PRIVATE_KEY = get_private_key() 
PUBLIC_KEY  = get_public_key()

class Word(models.Model):
    key       = models.CharField(max_length=200)
    word      = models.BinaryField(max_length=200)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.word

    @classmethod
    def delete_all_records(cls):
        [record.delete() for record in cls.objects.all()]

    @classmethod
    def save_word_histogram(cls, counter):
        ## TODO - fix this, there is bound to be a more efficient way in doing
        ## this, so brute force for now and optimise later
        public_key   = PUBLIC_KEY
        all_words    = cls.objects.all()
        update_words = []
        
        ## 1. Iterate through the words
        for word, frequency in counter:
            is_new = True
            ## 2. Check words that are already saved, if so update it
            for w in all_words:
                ## Since word is already encrypted, we compare encrypted
                ##  versions, this is not really a good idea - we should 
                ##  really be using the key (marked as a hash)
                if w.word == encrypt(word, public_key):
                    w.frequency = w.frequency + frequency
                    update_words.append(w)
                    is_new = False
                    break

            ## 3. If we cant find the word in the db, create a new one
            if is_new:
                new_word = cls(key=salted_hash(word),
                           word=encrypt(word, public_key), 
                           frequency=frequency)
                update_words.append(new_word)

        ## 4. Now we have our updated list, let's save it
        [w.save() for w in update_words]

    @classmethod
    def fetch_word_histogram(cls):
        ## 1. Grab objects from the database 
        private_key = PRIVATE_KEY
        words       = cls.objects.all()
        ## 2. Decrypt the words
        decrypted_words = [(decrypt(w.word, private_key), w.frequency) for w in words]
        ## 3. ... And sort
        return sorted(decrypted_words, key=lambda c: c[1], reverse=True)


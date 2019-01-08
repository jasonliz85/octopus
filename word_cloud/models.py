from django.db import models

def encrypt(word):
    return word

def decrypt(word):
    return word

def salted_hash(word):
    ## take note of random seeding
    ## os.environ['PYTHONHASHSEED'] 
    return hash(word)

class Word(models.Model):
    key       = models.CharField(max_length=200)
    word      = models.CharField(max_length=200)
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
        all_words = cls.objects.all()
        update_words = []
        for word, frequency in counter:
            is_new = True
            for w in all_words:
                if decrypt(w.word) == word:
                    print(word, frequency)
                    w.frequency = w.frequency + frequency
                    update_words.append(w)
                    is_new = False
                    break

            if is_new:
                new_word = cls(key=salted_hash(word),
                           word=encrypt(word), 
                           frequency=frequency)
                update_words.append(new_word)

        ## save the data
        [w.save() for w in update_words]

    @classmethod
    def fetch_word_histogram(cls):
        #de-encrypt
        words = cls.objects.all()
        return [(decrypt(w.word), w.frequency) for w in words]


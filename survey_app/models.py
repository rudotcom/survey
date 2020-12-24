from django.db import models


class Survey(models.Model):
    """ Опрос """
    survey_title = models.CharField('Опрос', max_length=100,
                                    null=False,
                                    default=None,
                                    blank=False)
    start_date = models.DateField('Дата старта', auto_now_add=True)
    finish_date = models.DateField('Дата окончания')
    description = models.TextField('Описание',
                                   null=True,
                                   default=None,
                                   blank=True)

    def __unicode__(self):
        return self.survey_title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """ Вопрос опроса с выбором типа полей (text, radio, checkbox)"""
    ANSWER_TEXT = 'AT'
    ANSWER_ONE = 'AO'
    ANSWER_MANY = 'AM'
    AnswerType = [
        (ANSWER_TEXT, 'Ответ с текстом'),
        (ANSWER_ONE, 'Ответ с одним выбором'),
        (ANSWER_MANY, 'Ответ с множественным выбором'),
    ]
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField('Вопрос', max_length=200)
    question_type = models.CharField('Тип ответа', max_length=2, choices=AnswerType, default=ANSWER_TEXT, )

    def __unicode__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """ Вариант ответа на вопрос Qusestion"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField('Ответ', max_length=200,
                                   null=False,
                                   default=None,
                                   blank=False)

    def __unicode__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class User(models.Model):
    user_ID = models.CharField(max_length=10, )


class UserAnswerChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, null=False, default=None, blank=False)

    def __unicode__(self):
        return self.answer_text

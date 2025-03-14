# Для начала импортирую все модели:
from news.models import *

# Создаю двух пользователей:
user1 = User.objects.create_user('lara_croft', 'lcro@exam.ru', 'password123')
user2 = User.objects.create_user('remark132', 'erixrem@exam.ru', 'password555')

# Создаю два объекта Author, связанные с пользователями:
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавляю 4 категории:
category1 = Category.objects.create(name='Politics')
category2 = Category.objects.create(name='Sports')
category3 = Category.objects.create(name='Technology')
category4 = Category.objects.create(name='Economics')

# Добавляю 2 статьи и одну новость:
post1 = Post.objects.create(author=author1, post_type='AR', title='Маржинальный анализ и его роль в принятии управленческих решений',
                           text='Маржинальный анализ — это метод экономического моделирования, оценки и обоснования эффективности управленческих решений в бизнесе.'
                                'Он базируется на изучении соотношения между тремя группами важнейших экономических показателей: издержками, объёмом производства (реализации) продукции и прибылью. '
                                'Также анализ позволяет прогнозировать величину каждого из этих показателей при заданном значении других.')
post2 = Post.objects.create(author=author2, post_type='AR', title='Как искусственный интелект заменил нам предподавателей',
                            text='Искусственный интеллект (ИИ) — это направление современной науки, которое изучает способы обучить компьютер, роботизированную технику, аналитическую систему разумно мыслить подобно человеку.'
                                 'В основе ИИ лежат методы сбора, обработки и анализа больших объёров данных. '
                                 'Чем больше информации получает ИИ-система, тем точнее она может распознавать закономерности и тренды, необходимые для принятия решений')
news1 = Post.objects.create(author=author1, post_type='NW', title='Стефан Карри стал лучшим шутером в истории НБА',
                            text='В 2020 году бывший президент США Барак Обама заявил, что Карри из «Голден Стэйт Уорриорз» — лучший шутер в истории лиги. '
                                 'Обама отметил, что не видел никого, кто мог бы бросать так же, как Карри, столькими разными способами и в разных ситуациях.!')

# Присваиваю категории статьям и новости:
PostCategory.objects.create(post=post1, category=category4)
PostCategory.objects.create(post=post1, category=category1)
PostCategory.objects.create(post=post2, category=category3)
PostCategory.objects.create(post=post2, category=category1)
PostCategory.objects.create(post=news1, category=category2)

# Создаю комментарии к объектам модели Post:
comment1 = Comment.objects.create(post=post1, user=user2, text='Познавательная статья!')
comment2 = Comment.objects.create(post=post2, user=user1, text='ИИ рулит!')
comment3 = Comment.objects.create(post=post2, user=user2, text='ИИ-замечательный инструмент')
comment4 = Comment.objects.create(post=news1, user=user1, text='Шеф Карри лучший!!!')

# Применяя функции like() и dislike() к статьям/новостям и комментариям,
# корректирую рейтинги этих объектов:
post1.like()
post1.like()
post1.dislike()
post2.like()
post2.like()

comment1.like()
comment2.dislike()

# Обновляю рейтинги пользователей:
author1.update_rating()
author2.update_rating()

# Вывожу username и рейтинг лучшего пользователя:
best_author = Author.objects.order_by('-rating').values('user__username', 'rating').first()
best_author


# Вывожу лучший пост на основе лайков и дислайков:
best_post = Post.objects.order_by('-rating').values('created_at','author__user__username', 'rating', 'title').first()



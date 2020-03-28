import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot("1126043908:AAGsfBWGOrl35xSs-OTOw1f_v8OBbt30_a0")


@bot.message_handler(commands=['contact'])
def contact(message):
  bot.send_message(message.chat.id, "You can contact me <b>@YeZzT</b>".format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Planche")
    item2 = types.KeyboardButton("Dynamics")
    item3 = types.KeyboardButton("Homework")
    item4 = types.KeyboardButton("Front Lever")
    item5 = types.KeyboardButton("Cardio")
    item6 = types.KeyboardButton("Challenge")
    #item7 = types.KeyboardButton("Basic movements, gain muscle")
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     "Hi there, <b>{0.first_name}</b>❗️\nMe - <b>{1.first_name}</b>, bot which was created to learn new skills in Workout.\n\nWe constantly have new updates, so don't forget to update bot regularly❗️\n\nVersion - testing now.".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Наши инлайновые кнопки
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Homework':
            bot.send_message(message.chat.id, 'Удачи тебе❗️ Про тренировки не забывай❗️')
        elif message.text == 'Cardio':
            markup = types.InlineKeyboardMarkup(row_width=2)
            finish = types.InlineKeyboardButton("Done", callback_data='finish1')
            lenb = types.InlineKeyboardButton("I'm lazy", callback_data='lenb1')

            markup.add(finish, lenb)
            bot.send_message(message.chat.id, 'Ты выбрал <b>Cardio</b>❗️ Вот твоя  тренировка:\n\n1. Бёрпи - ' + str(random.randint(10,15)) +' повторений\nОтдых 15 секунд. \n\n2. Медленные отжимание - ' + str(random.randint(10,15)) + ' повторений\nОтдых 15 секунд.\n\n3. Отжимания 2х2х2, задерживаемся в нижней, средней и верхней точке 2 секунды - ' + str(random.randint(8,12)) +' повторений\n Отдых 15 секунд.\n\n4. Отжимания - ' + str(random.randint(10,15)) + ' повторений\nОтдых 15 секунд.\n\n5. Приседания с прыжком и задержкой 3 секунды в низу - ' + str(random.randint(10,20)) + ' повторений\nОтдых 15 секунд.\n\n6. Медленные приседания - ' + str(random.randint(8,15)) + ' повторений\nОтдых 15 секунд.\n\n7. Ножницы на пресс - ' + str(random.randint(20,30)) + ' раз\nОтдых 15 секунд.\n\n8. Велосипед - ' + str(random.randint(20,30)) + ' раз\nОтдых 15 секунд.\n\n9. Скручивания с задержкой в точке с пиковой нагрузкой - ' + str(random.randint(10,20)) + ' повторений\nОтдых 15 секунд.\n\n10. Планка на локтях - 30 секунд\nОтдых 15 секунд.\n\n11. Х-прыжки - ' + str(random.randint(15,30)) + ' раз\nОтдых 15 секунд.\n\n12. Бёрпи - ' + str(random.randint(10,15)) + ' повторений\n\nПострой своё тело повторение за повторением❗️', reply_markup=markup, parse_mode='html')            
        elif message.text == 'Challenge':
            markup = types.InlineKeyboardMarkup(row_width=2)
            push = types.InlineKeyboardButton("Push", callback_data='push1')
            pull = types.InlineKeyboardButton("Pull", callback_data='pull1')
            daily = types.InlineKeyboardButton("Daily", callback_data='daily1')
            week = types.InlineKeyboardButton("Weekly", callback_data='week1')


            markup.add(push, pull, daily, week)
            bot.send_message(message.chat.id, 'Раздел Challenge проверит твои силы❗️', reply_markup=markup)     
        elif message.text == 'LOLbKA':
            bot.send_message(message.chat.id, 'Ах ты ж лоликонщик❗️ Ану пошёл тренить, нечего лолек трогать❗️')   
        elif message.text == 'J_U':
            bot.send_message(message.chat.id, 'Секретный символ знаешь, молодец.\n\nСкоро здесь появятся подсказки к секретным командам❗️')                   
        elif message.text == 'Dynamics':
            markup = types.InlineKeyboardMarkup(row_width=2)
            sklepka = types.InlineKeyboardButton("Склёпка", callback_data='sklepka1')
            zamok = types.InlineKeyboardButton("Замок", callback_data='zamok1')

            markup.add(sklepka, zamok)
            bot.send_message(message.chat.id, 'Ты выбрал динамику❗️ Выбери, что будешь учить:', reply_markup=markup)
        elif message.text == 'Front Lever':

            markup = types.InlineKeyboardMarkup(row_width=2)
            newone = types.InlineKeyboardButton("New", callback_data='new')
            interone = types.InlineKeyboardButton("Intermidiate", callback_data='inter')

            markup.add(newone, interone)

            bot.send_message(message.chat.id, 'Ты выбрал <b>Front Lever</b>❗️ Теперь укажи свой уровень: ', parse_mode = 'html',
                             reply_markup=markup)
        elif message.text == 'Planche':
            markup = types.InlineKeyboardMarkup(row_width=2)
            newto = types.InlineKeyboardButton("New", callback_data='new1')
            interto = types.InlineKeyboardButton("Intermidiate", callback_data='inter1')

            markup.add(newto, interto)
            bot.send_message(message.chat.id, 'Ты выбрал <b>Planche</b>❗️ Теперь укажи свой уровень:', parse_mode = 'html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Введите правильный запрос.')


# Исходное сообщение
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'sklepka1':
                bot.send_message(call.message.chat.id,
                                 'Видео, в котором учтены все ошибки. \nГлавная проблема - сгибание рук, не сгибайте руки при залёте на труник.\n\nhttps://www.youtube.com/watch?v=W6VRWt8OZFQ',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Dynamics</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'zamok1':
                bot.send_message(call.message.chat.id,
                                 'Основной ошибкой является неправильная раскачка.\nПодробнее в видео\n\nhttps://www.youtube.com/watch?v=GvJe3MVk6tY',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Dynamics</b>:", parse_mode='html',
                                      reply_markup=None)      
            elif call.data == 'finish1':
                bot.send_message(call.message.chat.id,
                                 'Просто красавчик, 30 минут боли🔥 сегодня, подарят тебе гордость на всю жизнь❗️\n\nПродолжай работать вместе со мной❗️')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Хорошая работа❗️ Так держать❗️🚀",
                                      reply_markup=None)      
            elif call.data == 'lenb1':
                bot.send_message(call.message.chat.id,
                                 'Не ленись, ведь твоя работа сегодня - это твой вклад🚀 в завтра.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Надеюсь, ты ошибся кнопкой)",
                                      reply_markup=None)     
            elif call.data == 'push1':
                bot.send_message(call.message.chat.id,
                                 'Готовся, сейчас будет 🔥месиво❗️ Bring Sally Up Challenge проверит не только твою физическую подготовку, но и реально заставит боротся за каждую секунду❗️\n\nУсловия, включаем песню/видео и занимаем позицию отжиманий. Когда в песне поют "Bring Sally Down" мы опускаемся вниз и удерживаем позицию без касания пола, когда поют "Bring Sally Up" мы переходим на вытянутые руки.\n\nПример в видео ниже. Хорошей тренировки!\n\nНе переживай, если что-то не выходит с первого раза, это лишь ещё одна возможность стать лучше❗️\n\nhttps://www.youtube.com/watch?v=41N6bKO-NVI')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Bring Sally Up Challenge</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'pull1':
                bot.send_message(call.message.chat.id,
                                 'Сейчас будет 🔥жарко❗️\n\n1. Подтягивания 3х3х3, в нижней, средней и пиковой точке задержка на 3 секунды - 5 раз\n\n2. Подятгивания с медленным опусканием - 5 раз\n\n3. Подтягивания - 5 раз\n\n4. Подведение носков к турнику - 10 раз\n\nВыполняем все упражнения не слазя с турника!\n\nНе переживай, если что-то не выходит с первого раза, это лишь ещё одна возможность стать лучше!')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Super pull set</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'daily1':
                bot.send_message(call.message.chat.id,
                                 'Новый день - новый <b>Challenge</b>.❗️\n\nУже умеешь приседать на 1 ноге? И на правой и на левой? Если да, то завтра будет новый недельный 🔥челлендж, если нет, то самое время попробовать❗️\n\nПрокачайся🚀 за карантин❗️', parse_mode = 'html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Daily Challenge</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'week1':
                bot.send_message(call.message.chat.id,
                                 'Challenge на неделю - отжимание🦾 в течении 1 минуты. Тебе нужно взять таймер сделать 1 отжиманиев течении минуты, постарайся сделать фазу опускания и фазу подъёма равными по 30 секунд❗️\n\nУдачи, у тебя целая неделя, что бы затащить❗️')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Weekly Challenge</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'new':
                bot.send_message(call.message.chat.id,
                                 'Front Lever <b>Level 1</b>.\n\nСначала разберёмся с техникой. Руки всегда прямые, стараемся избегать сгибаний в локтях. При идеальной форме тело должно идти одной линией, без прогибов в пояснице, лопатки сведены.\n\nТеперь перейдём к тренировке.\n\n1. Подтягивания 5-10 повторений 4 подхода.\n\n2. Сведение лопаток, висим на турнике и сводим лопатки вертикальным движением корпуса вверх, 10-15 повторений на 3 подхода.\n\n3. Ноги к перекладине. С положения виса на турнике поднимает ноги и пытаемся коснутся носками турника 3 подхода по 8 повторений.\n\n4. С положения виса на турнике сгибаем ноги в коленях и подводим к пресу, удерживаем 15-20 секунд на 4 подхода.', parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Front Lever</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'inter':
                bot.send_message(call.message.chat.id,
                                 'Front Lever <b>Level 2</b>.\n\n0. Начнём с попыток. Для начала пробуем держать передний вис, 10-15 попыток\n\n1. Поднимаем колени к груди и занимаем позицию переднего виса, выпрямляем ноги и опускаемся максимально медленно. Повторяем 10-15 раз.\n\n2. Поднимаем колени к груди и принимаем положение переднего виса. Держим такую позицию 20 секунд.\n\n3. Подтягивания в уголке 3-8 раз.\n\n4. Носки к турнику 10-15 повторений.\n\n5. С положения виса сводим лопатки и пытаемся приподнять корпус, 10 повторений.\n\nДелаем 2 таких круга, отдых между всеми упражнениями 90 секунд.', parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Front Lever</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'new1':
                bot.send_message(call.message.chat.id,
                                 'Planche <b>Level 1</b>.\n\nДля начала разберёмся с правильной формой.\n1. При планше руки должны быть прямые, без сгибаний в локтях.\n\n2. Лопатки разведены, создаём небольшой горб на спине.\n\n3. Взгляд направлен вперёд.\n\nhttps://www.youtube.com/watch?v=POq_-CTIX3o&t=263s', parse_mode = 'html')
                bot.send_message(call.message.chat.id,
                                 'Теперь можно начать тренировку.\n\n1. Занимаем положение упор лёжа и пытаемся накатитя плечами максимально вперёд, делаем отжимания 3 подхода на 1-2 повторений.\n\n2. Накатываем плечи вперёд и удерживаем положение максимальное время на 3 подхода.\n\n3. Накаты плечами вперёд, как можно дальше, из положения упора лёжа, затем возвращаемся в стартовое положение, 10 раз.\n\n4. Становимся на колени и повторяем предыдущее упражнение с колен.\n\n\nВсегда следи, что бы руки были прямыми❗️\n\nДелаем таких 2 круга❗️ После первого круга отдых 2 минуты❗️ Отдых 60-90 секунд между упражнениями❗️', parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Planche</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'inter1':
                bot.send_message(call.message.chat.id,
                                 'Planche <b>Level 2</b>.\n\nНачнём тренировку❗️\n\n0. Перед началом попробуем сделать планш, 5-8 попыток.\n\n1. Накатываемся плечами вперёд, поднимаем таз и пытаемся подойти ногами как можно ближе к рукам, возвращаемся в исходное положение, 3 подхода на 7-10 повторений.\n\n2. Накатываем плечи вперёд и делаем 5-7 отжиманий на 4 подхода.\n\n3. Накатываем плечи и держим 20-30 секунд.\n\nДелаем 2 таких круга, после чего делаем упражнение №4.\n\n4. Ставим руки по шире и накатываем плечи вперёд, держим на максимум 5 раз.\n\nВсегда следите за прямыми руками❗️ Отдых между кругами 2 минуты❗️', parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Planche</b>:", parse_mode='html',
                                      reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot("789322878:AAH7ggVSnFoo6ssXSgAXpv5y6GFnLCW2DAE")


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Dynamics")
    item2 = types.KeyboardButton("Planche")
    item3 = types.KeyboardButton("Front Lever")
    item4 = types.KeyboardButton("Пойду делать домашку")
    item5 = types.KeyboardButton("Кардио")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для изучения новых элементов воркаута.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Наши инлайновые кнопки
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Пойду делать домашку':
            bot.send_message(message.chat.id, 'Удачи тебе! Про тренировки не забывай!')
        elif message.text == 'Кардио':
            markup = types.InlineKeyboardMarkup(row_width=4)
            pushup = types.InlineKeyboardButton("Взрывные отжимания", callback_data='pushup1')
            squat = types.InlineKeyboardButton("Взрывные приседания", callback_data='squat1')

            markup.add(pushup, squat)
            bot.send_message(message.chat.id, 'Ты выбрал Кардио! Для хорошей тренировки выполни 5 кругов каждого упражнения!\n\nВыбери себе упражнение:', reply_markup=markup)            
        elif message.text == 'Dynamics':
            markup = types.InlineKeyboardMarkup(row_width=2)
            sklepka = types.InlineKeyboardButton("Склёпка", callback_data='sklepka1')
            zamok = types.InlineKeyboardButton("Замок", callback_data='zamok1')

            markup.add(sklepka, zamok)
            bot.send_message(message.chat.id, 'Ты выбрал динамику! Выбери, что будешь учить:', reply_markup=markup)
        elif message.text == 'Front Lever':

            markup = types.InlineKeyboardMarkup(row_width=2)
            newone = types.InlineKeyboardButton("Новичок", callback_data='new')
            interone = types.InlineKeyboardButton("Средний", callback_data='inter')

            markup.add(newone, interone)

            bot.send_message(message.chat.id, 'Ты выбрал передний вис! Теперь укажи свой уровень: ',
                             reply_markup=markup)
        elif message.text == 'Planche':
            markup = types.InlineKeyboardMarkup(row_width=2)
            newto = types.InlineKeyboardButton("Новичок", callback_data='new1')
            interto = types.InlineKeyboardButton("Средний", callback_data='inter1')

            markup.add(newto, interto)
            bot.send_message(message.chat.id, 'Ты выбрал планш! Теперь укажи свой уровень:', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Введите правильный запрос')


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
                                      text="Учим динамику:",
                                      reply_markup=None)
            elif call.data == 'zamok1':
                bot.send_message(call.message.chat.id,
                                 'Основной ошибкой является неправильная раскачка.\nПодробнее в видео\n\nhttps://www.youtube.com/watch?v=GvJe3MVk6tY',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Учим динамику:",
                                      reply_markup=None)
            elif call.data == 'pushup1':
                bot.send_message(call.message.chat.id,
                                 'Твоё упражнение -- взрывное отжимание, количевство раз - ' + str(random.randint(1,30)) + '.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Кардио:",
                                      reply_markup=None)    
            elif call.data == 'squat1':
                bot.send_message(call.message.chat.id,
                                 'Твоё упражнение -- взрывное приседание, количевство раз - ' + str(random.randint(1,30)) + '.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Кардио:",
                                      reply_markup=None)                                                
            elif call.data == 'new':
                bot.send_message(call.message.chat.id,
                                 'Передний вис Уровень 1.\n\nСначала разберёмся с техникой. Руки всегда прямые, стараемся избегать сгибаний в локтях. При идеальной форме тело должно идти одной линией, без прогибов в пояснице, лопатки сведены.\n\nТеперь перейдём к тренировке.\n\n1. Подтягивания 5-10 повторений 4 подхода.\n\n2. Сведение лопаток, висим на турнике и сводим лопатки вертикальным движением корпуса вверх, 10-15 повторений на 3 подхода.\n\n3. Ноги к перекладине. С положения виса на турнике поднимает ноги и пытаемся коснутся носками турника 3 подхода по 8 повторений.\n\n4. С положения виса на турнике сгибаем ноги в коленях и подводим к пресу, удерживаем 15-20 секунд на 4 подхода.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Учим передний вис:",
                                      reply_markup=None)
            elif call.data == 'inter':
                bot.send_message(call.message.chat.id,
                                 'Передний вис Уровень 2.\n\n0. Начнём с попыток. Для начала пробуем держать передний вис, 10-15 попыток\n\n1. Поднимаем колени к груди и занимаем позицию переднего виса, выпрямляем ноги и опускаемся максимально медленно. Повторяем 10-15 раз.\n\n2. Поднимаем колени к груди и принимаем положение переднего виса. Держим такую позицию 20 секунд.\n\n3. Подтягивания в уголке 3-8 раз.\n\n4. Носки к турнику 10-15 повторений.\n\n5. С положения виса сводим лопатки и пытаемся приподнять корпус, 10 повторений.\n\nДелаем 2 таких круга, отдых между <b>всеми</b> упражнениями 90 секунд.')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Учим передний вис:",
                                      reply_markup=None)
            elif call.data == 'new1':
                bot.send_message(call.message.chat.id,
                                 'Планш <b>Уровень 1.</b>\n\nДля начала разберёмся с правильной формой.\n1. При планше руки должны быть прямые, без сгибаний в локтях.\n\n2. Лопатки разведены, создаём небольшой горб на спине.\n\n3. Взгляд направлен вперёд.',
                                 parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 'Теперь можно начать тренировку.\n\n1. Занимаем положение упор лёжа и пытаемся накатитя плечами максимально вперёд, делаем отжимания 3 подхода на 1-2 повторений.\n\n2. Накатываем плечи вперёд и удерживаем положение максимальное время на 3 подхода.\n\n3. Накаты плечами вперёд, как можно дальше, из положения упора лёжа, затем возвращаемся в стартовое положение, 10 раз.\n\n4. Становимся на колени и повторяем предыдущее упражнение с колен.\n\n\nВсегда следи, что бы руки были прямыми!\n\nДелаем таких 2 круга! После первого круга отдых 2 минуты! Отдых 60-90 секунд между упражнениями!')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Учим планш:",
                                      reply_markup=None)
            elif call.data == 'inter1':
                bot.send_message(call.message.chat.id,
                                 'Планш Уровень 2.\n\nНачнём тренировку!\n\n0. Перед началом попробуем сделать планш, 5-8 попыток.\n\n1. Накатываемся плечами вперёд, поднимаем таз и пытаемся подойти ногами как можно ближе к рукам, возвращаемся в исходное положение, 3 подхода на 7-10 повторений.\n\n2. Накатываем плечи вперёд и делаем 5-7 отжиманий на 4 подхода.\n\n3. Накатываем плечи и держим 20-30 секунд.\n\nДелаем 2 таких круга, после чего делаем упражнение №4.\n\n4. Ставим руки по шире и накатываем плечи вперёд, держим на максимум 5 раз.\n\nВсегда следите за прямыми руками! Отдых между кругами 2 минуты! ')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Учим планш:",
                                      reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

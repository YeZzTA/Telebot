import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot("1126043908:AAGsfBWGOrl35xSs-OTOw1f_v8OBbt30_a0")


@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, "You can contact me <b>@YeZzT</b>".format(message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'I have a large amount of options to discover. If you are new to Workout, '
                                      'I would rocommend you to read <b>Technique</b> guide.\n\nAfter that you can '
                                      'continue discovering Workout world with another sections.',
                     parse_mode='html')


@bot.message_handler(commands=['update'])
def update(message):
    bot.send_message(message.chat.id, 'Something new is coming❗',
                     parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Planche")
    item2 = types.KeyboardButton("Dynamics")
    item3 = types.KeyboardButton("Technique")
    item4 = types.KeyboardButton("Front Lever")
    item5 = types.KeyboardButton("Cardio")
    item6 = types.KeyboardButton("Challenge")
    item7 = types.KeyboardButton("Basic movements, gain muscle")
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     "Hi there, <b>{0.first_name}</b>❗️\nMe - <b>{1.first_name}</b>, bot which was created to learn "
                     "new skills in Workout.\n\nWe constantly have new updates, so don't forget to update bot "
                     "regularly❗️\n\nVersion - testing now.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Наши инлайновые кнопки
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Technique':
            markup = types.InlineKeyboardMarkup(row_width=2)
            pushups = types.InlineKeyboardButton("Push-ups", callback_data='pushups')
            pullups = types.InlineKeyboardButton("Pull-ups", callback_data='pullups')

            markup.add(pushups, pullups)
            bot.send_message(message.chat.id, 'Выбери скилл, которому хочешь научиться:', reply_markup=markup)
        elif message.text == 'Basic movements, gain muscle':
            markup = types.InlineKeyboardMarkup(row_width=2)
            bazapush = types.InlineKeyboardButton("Push ups", callback_data='bazapush')
            bazapull = types.InlineKeyboardButton("Pull ups", callback_data='bazapull')
            bazachest1 = types.InlineKeyboardButton("Chest LvL 1", callback_data='bazachest1')
            bazaspina1 = types.InlineKeyboardButton("Back LvL 1", callback_data='bazaspina1')
            bazachest2 = types.InlineKeyboardButton("Chest LvL 2", callback_data='bazachest2')
            bazaspina2 = types.InlineKeyboardButton("Back LvL 2", callback_data='bazaspina2')
            bazachest3 = types.InlineKeyboardButton("Chest LvL 3", callback_data='bazachest3')
            bazaspina3 = types.InlineKeyboardButton("Back LvL 3", callback_data='bazaspina3')
            bazanogi1 = types.InlineKeyboardButton("Legs LvL 1", callback_data='bazanogi1')
            bazapress1 = types.InlineKeyboardButton("Abs LvL 1", callback_data='bazapress1')
            bazanogi2 = types.InlineKeyboardButton("Legs LvL 2", callback_data='bazanogi2')
            bazapress2 = types.InlineKeyboardButton("Abs LvL 2", callback_data='bazapress2')
            bazanogi3 = types.InlineKeyboardButton("Legs LvL 3", callback_data='bazanogi3')
            bazapress3 = types.InlineKeyboardButton("Abs LvL 3", callback_data='bazapress3')

            markup.add(bazapush, bazapull, bazachest1, bazaspina1, bazachest2, bazaspina2, bazachest3, bazaspina3,
                       bazanogi1, bazapress1, bazanogi2, bazapress2, bazanogi3, bazapress3)
            bot.send_message(message.chat.id,
                             'Прокачай базовые движения, набери массу! Не забудь сделать тщательную разминку перед '
                             '🔥тренировкой, чтобы избежать травм❗️ Выбери упражнение или группу мышц, которую хочешь '
                             'проработать:',
                             reply_markup=markup)

        elif message.text == 'Cardio':
            markup = types.InlineKeyboardMarkup(row_width=2)
            finish = types.InlineKeyboardButton("Done", callback_data='finish1')
            lenb = types.InlineKeyboardButton("I'm lazy", callback_data='lenb1')

            markup.add(finish, lenb)
            bot.send_message(message.chat.id, 'Ты выбрал <b>Cardio</b>❗️ Вот твоя  тренировка:\n\n1. Бёрпи - ' + str(
                random.randint(10, 15)) + ' повторений\nОтдых 15 секунд. \n\n2. Медленные отжимание - ' + str(
                random.randint(10,
                               15)) + 'повторений\nОтдых 15 секунд.\n\n3. Отжимания 2х2х2, задерживаемся в нижней, '
                                      'средней и верхней точке 2 секунды - ' + str(
                random.randint(8, 12)) + ' повторений\n Отдых 15 секунд.\n\n4. Отжимания - ' + str(random.randint(10,
                                                                                                                  15)) + ' повторений\nОтдых 15 секунд.\n\n5. Приседания с прыжком и задержкой 3 секунды в низу - ' + str(
                random.randint(10, 20)) + ' повторений\nОтдых 15 секунд.\n\n6. Медленные приседания - ' + str(
                random.randint(8, 15)) + ' повторений\nОтдых 15 секунд.\n\n7. Ножницы на пресс - ' + str(
                random.randint(20, 30)) + ' раз\nОтдых 15 секунд.\n\n8. Велосипед - ' + str(random.randint(20,
                                                                                                           30)) + 'раз\nОтдых 15 секунд.\n\n9. Скручивания с задержкой в точке с пиковой нагрузкой - ' + str(
                random.randint(10,
                               20)) + 'повторений\nОтдых 15 секунд.\n\n10. Планка на локтях - 30 секунд\nОтдых 15 '
                                      'секунд.\n\n11. Х-прыжки - ' + str(
                random.randint(15, 30)) + ' раз\nОтдых 15 секунд.\n\n12. Бёрпи - ' + str(
                random.randint(10, 15)) + ' повторений\n\nПострой своё тело повторение за повторением❗️',
                             reply_markup=markup, parse_mode='html')

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
            bot.send_message(message.chat.id,
                             'Секретный символ знаешь, молодец.\n\nСкоро здесь появятся подсказки к секретным '
                             'командам❗️')

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

            bot.send_message(message.chat.id, 'Ты выбрал <b>Front Lever</b>❗️ Теперь укажи свой уровень: ',
                             parse_mode='html',
                             reply_markup=markup)

        elif message.text == 'Planche':
            markup = types.InlineKeyboardMarkup(row_width=2)
            newto = types.InlineKeyboardButton("New", callback_data='new1')
            interto = types.InlineKeyboardButton("Intermidiate", callback_data='inter1')

            markup.add(newto, interto)
            bot.send_message(message.chat.id, 'Ты выбрал <b>Planche</b>❗️ Теперь укажи свой уровень:',
                             parse_mode='html', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Введите правильный запрос.')


# Исходное сообщение
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'bazapush':
                bot.send_message(call.message.chat.id,
                                 'Чтобы увеличить количевство 🔥отжиманий, нужно прокачать нашу выносливость в этом упражнении, то есть подразумевается <b>длительное время под нагрузкой</b>.\n\nНачнём тренировку❗️\n\n0. Сначала разминка, как следует разомни мышцы, чтобы избежать травм и выдать лучший результат.\n\n1. Делаем отжимания на максимум🚀 и записываем свой результат.\n\n2. Делаем отжимание в течении 1 минуты, 30 секунд опускаемся, 30 поднимаемся. Делаем таких 2-3 раза❗️ Отдых 3-4 минуты.\n\n3. Берём во внимание результат из первого упражнения. Делим количевство повторений на пополам и пытаемся сделать. Например, в первом упражнении у меня 50, значит в 3 я должен сделать 25.\n\nЕсли, ты сделал все повторения🚀 в 3 упражнении, то есть половину от своего максимального, тогда в следующий раз ты делаешь новый подход на максимум.\n\nЕсли нет, тогда оставляешь свой максимум и тренируешся пока не сделаешь 3 упражнение.\n\nТаким образом ты задаёшь тонус своим мышцам и прокачиваешь выносливость🔥 на всех этапах тренировки, в начале, когда ты полон сил и в конце, когда мышцы уже устали.\n\nБорись до конца в каждом подходе и результат🚀 обязательно прийдёт. Увидимся в лучшей форме❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Увеличь количевство отжиманий</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazapull':
                bot.send_message(call.message.chat.id,
                                 'Увеличить количевство подтягиваний🔥 можно поработав над нашей <b>фазой опускания</b>, которая просто пропускается при выполнении на количевство.\n\nДля этого выполним лесенку, в которой немного изменим форму выполнения упражнения.\n\n<b>Форма</b>: Подтягиваемся, заводя подбородок над перекладиной и затем медленно опускаемся, разтягивая время опускания на 2-3 секунды❗️ Время отдыха между подходами регулируем обычным счётом, то есть, если только что было 5, то умножаем количевство на 2 и считаем про себя, будет 10 счётов для отдыха❗️\n\nРаботаем в таком стиле и да прибудет с вами 🚀прогресс❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Увеличь количевство подтягиваний</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazachest':
                markup = types.InlineKeyboardMarkup(row_width=2)
                bazachest1 = types.InlineKeyboardButton("Chest LvL 1", callback_data='bazachest1')
                bazachest2 = types.InlineKeyboardButton("Chest LvL 2", callback_data='bazachest2')
                bazachest3 = types.InlineKeyboardButton("Chest LvL 3", callback_data='bazachest3')

                markup.add(bazachest1, bazachest2, bazachest3)

                bot.send_message(call.message.chat.id,
                                 '<b>Тренировка на грудные и трицепс❗️ Выбери свой уровень</b>:', parse_mode='html',
                                 reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка на грудные и трицепс</b>:", parse_mode='html',
                                      reply_markup=markup)

            elif call.data == 'bazaspina':
                markup = types.InlineKeyboardMarkup(row_width=2)
                bazaspina1 = types.InlineKeyboardButton("Back LvL 1", callback_data='bazaspina1')
                bazaspina2 = types.InlineKeyboardButton("Back LvL 2", callback_data='bazaspina2')
                bazaspina3 = types.InlineKeyboardButton("Back LvL 3", callback_data='bazaspina3')

                markup.add(bazaspina1, bazaspina2, bazaspina3)

                bot.send_message(call.message.chat.id,
                                 '<b>Тренировка спины и плечей❗️ Выбери свой уровень</b>:', parse_mode='html',
                                 reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка спины и плечей</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'bazanogi':
                markup = types.InlineKeyboardMarkup(row_width=2)
                bazanogi1 = types.InlineKeyboardButton("Legs LvL 1", callback_data='bazanogi1')
                bazanogi2 = types.InlineKeyboardButton("Legs LvL 2", callback_data='bazanogi2')
                bazanogi3 = types.InlineKeyboardButton("Legs LvL 3", callback_data='bazanogi3')

                markup.add(bazanogi1, bazanogi2, bazanogi3)

                bot.send_message(call.message.chat.id,
                                 '<b>Тренировка ног❗️ Выбери свой уровень</b>:', parse_mode='html', reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка ног</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazapress':
                markup = types.InlineKeyboardMarkup(row_width=2)
                bazapress1 = types.InlineKeyboardButton("Abs LvL 1", callback_data='bazapress1')
                bazapress2 = types.InlineKeyboardButton("Abs LvL 2", callback_data='bazapress2')
                bazapress3 = types.InlineKeyboardButton("Abs LvL 3", callback_data='bazapress3')

                markup.add(bazapress1, bazapress2, bazapress3)

                bot.send_message(call.message.chat.id,
                                 '<b>Тренировка пресса❗️ Выбери свой уровень</b>:', parse_mode='html',
                                 reply_markup=markup)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка пресса</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazachest1':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. Отжимания🔥 широким постановкой 12 повторений. Руки сгибаем под 45 градусов, локти уходят в стороны❗️\n\n2. Отжимания, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Делаем 12 🔥повторений❗️\n\n3. Ставим руки вместе и делаем 🔥отжимания, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Локти идут вдоль тела❗️ Делаем 12 повторений❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️\n\nЕсли получилось сделать все повторения(12) в каждом🚀 из подходов, то переходим на LvL 2❗️')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка на грудные и трицепс LvL 1</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazachest2':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. Отжимания🔥 широким постановкой 12 повторений. Руки сгибаем под 45 градусов, локти уходят в стороны❗️ Движение вниз занимает 4 секунд, вверх 1 секунду❗️ Выполняем 12 повторений\n\n2. Ставим руки вместе и делаем 🔥отжимания, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Локти идут в стороны, напрягаем грудь❗️ Делаем 12 повторений❗️\n\n3. Отжимания, руки на ширине плеч, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Делаем 12 🔥повторений❗️\n\n4. Ставим руки вместе и делаем 🔥отжимания, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Локти идут вдоль тела, напрягаем трицепс❗️ Делаем 12 повторений❗️\n\n5. Отжимаемся🔥 и задерживаемся в нижней точке на максимальное время❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️\n\nЕсли получилось сделать все повторения(12) в каждом🚀 из подходов, то переходим на LvL 3❗️')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка на грудные и трицепс LvL 2</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazachest3':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. Отжимания🔥, ноги на возвышенности. Ставим ноги на возвышенности и делаем отжимания, 2-3 секунды вниз и 1 секунду вверх❗️ Выполняем 12 повторений❗️\n\n2. Взрывные отжимания. Выжимаем максимально быстро, что бы в верхней точке ладони оторвались от пола❗️ Делаем 12 повторений❗️\n\n3. Отжимания, руки на ширине плеч, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Делаем 12 🔥повторений❗️\n\n4. Ставим руки вместе и делаем 🔥отжимания, движение вниз занимает 4 секунды, а движение вверх 1 секунду. Локти идут вдоль тела, напрягаем трицепс❗️ Делаем 12 повторений❗️\n\n 5. Отжимаемся🔥 и задерживаемся в нижней точке на максимальное время❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️\n\nВ скором будущем выйдут новые уровни тренировки❗️')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка на грудные и трицепс LvL 3</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazaspina1':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n<b>Плечи</b>:\n\n1. <b>Армейские отжимания</b>. Становимся в позицию отжиманий и подводим ноги ближе к рукам, основную работу выполняют плечи, руки идут под 45 градусов в стороны❗️ Выполняем 8 повторений❗️\n\n2. <b>Касания плеча</b>. Становимся в позицию отжиманий и одной рукой касаемся противоположного плеча❗️ Выполняем 10 касаний к каждому плечу❗️\n\n<b>Спина</b>:\n\n3. <b>Подтягивания</b>. Подбородок над перекладиной❗️ Выполняем 8 повторений❗️\n\n4. <b>Подтягивания обратным хватом</b>. Подбородок над перекладиной❗️ Выполняем 8 повторений❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 120 секунд❗️\n\nЕсли получилось сделать все повторения(8/10) в каждом🚀 из подходов, то переходим на LvL 2❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренировка спины и плечей LvL 1</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazaspina2':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n<b>Плечи</b>:\n\n1. <b>Армейские отжимания</b>. Становимся в позицию отжиманий и подводим ноги ближе к рукам, основную работу выполняют плечи, руки идут под 45 градусов в стороны❗️ Движение вниз 2-3 секунды, вверх 1 секунда❗️ Выполняем 10 повторений❗️\n\n2. <b>Планш отжимания</b>. Становимся в позицию отжиманий и накатываем плечи вперёд, что бы ладони оказались на уровне груди❗️ Делаем 8 повторений❗️ Это не так просто, как кажется, будь окуратен с запястьями❗️\n\n3. <b>Касания плеча</b>. Становимся в позицию отжиманий и одной рукой касаемся противоположного плеча❗️ Выполняем 15 касаний к каждому плечу❗️\n\n<b>Спина</b>:\n\n4. <b>Подтягивания</b>. Подбородок над перекладиной❗️ Выполняем 10 повторений❗️\n\n5. <b>Подтягивания обратным хватом</b>. Подбородок над перекладиной❗️ Выполняем 10 повторений❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 120 секунд❗️\n\nЕсли получилось сделать все повторения(8/10/15/) в каждом🚀 из подходов, то переходим на LvL 3❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка спины и плечей LvL 2</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazaspina3':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n<b>Плечи</b>:\n\n1. <b>Армейские отжимания</b>. Становимся в позицию отжиманий и подводим ноги ближе к рукам, основную работу выполняют плечи, руки идут под 45 градусов в стороны❗️ Движение вниз 4 секунды, вверх 1 секунда❗️ Выполняем 12 повторений❗️\n\n2. <b>Планш отжимания</b>. Становимся в позицию отжиманий и накатываем плечи вперёд, что бы ладони оказались на уровне груди❗️ Делаем 10 повторений❗️ Пробуй ставить руки всё ближе к поясу, так ты изменишь действия силы и сможешь включить ещё больше мышц в работу❗️\n\n3. <b>Касания плеча</b>. Становимся в позицию отжиманий и одной рукой касаемся противоположного плеча❗️ Выполняем 20 касаний к каждому плечу❗️\n\n<b>Спина</b>:\n\n4. <b>Подтягивания</b>. Подбородок над перекладиной❗️ Выполняем 12 повторений❗️\n\n5. <b>Подтягивания обратным хватом</b>. Подбородок над перекладиной❗️ Выполняем 12 повторений❗️\n\n6. <b>Дельты и внутренняя часть спины</b>. Ложимся на живот, руки вытянуты вдоль тела. Приподымаем плечевой пояс и рукамы сжимаем лопатки, напрягая таким образом внутреннюю часть спины и дельтовидные мышцы, при сжатии удерживаем мышцы в напряжении 2-3 секунды❗️ Выполняем 20 повторений❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 120 секунд❗️\n\nВ скором будущем выйдут новые уровни тренировки❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка спины и плечей LvL 3</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazanogi1':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Приседания с 🔥прыжком + поворот</b>. Приседаем, затем высоко выпрыгиваем и делаем поворот на 180 градусов❗️ Выполняем 15 повторений❗️\n\n2. <b>Медленные приседания</b>. Опускаемся медленно вниз, в течении 3-5 секунд и 1 секунду вверх❗️ Выполняем 15 повторений❗️\n\n3. <b>Выпады</b>. Ноги всегда под углом 90 градусов, движение вниз 3 секунд, вверх 1 секунду❗️ Выполняем 20 повторений❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️\n\nЕсли получилось сделать все повторения(15/20) в каждом🚀 из подходов, то переходим на LvL 2❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка ног LvL 1</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazanogi2':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Приседания с 🔥прыжком + поворот</b>. Приседаем, затем высоко выпрыгиваем и делаем поворот на 180 градусов❗️ В нижней точке задерживаемся на 2 секунды❗️ Выполняем 20 повторений❗️\n\n2. <b>Приседания с весом</b>. Берём школьный или любой другой портфель и ложим туда пару книжек. Выполняем 15 повторений❗️\n\n3. <b>Удержание</b>. Приседаем до положения, пока тело не станет паралельно земле, между ногами и телом угл 90 градусов❗️ Удерживаем эту позицию 40 секунд❗️\n\n4. <b>Голень</b>. Берём какой-то предмет 10-15 см в высоту, на котором удобно стоять. Становимся возле стены и упираем руки, ставим носок 1 ноги на край премета, пятка должна быть ниже носка и почти дотрагиваться пола, с это положения выжимаем себя 1 ногой, затем медленно опускаемся в исходное положение и повторяем❗️ Выполняем 20 повторений на каждую ногу❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️\n\nЕсли получилось сделать все повторения(15/20) в каждом🚀 из подходов, то переходим на LvL 3❗️ ',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка ног LvL 2</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazanogi3':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Приседания с 🔥прыжком + поворот</b>. Приседаем, затем высоко выпрыгиваем и делаем поворот на 180 градусов❗️ В нижней точке задерживаемся на 3 секунды❗️ Выполняем 20 повторений❗️\n\n2. <b>Приседания с весом</b>. Берём школьный или любой другой портфель и ложим туда пару книжек. Стараемся увеличивать по немногу вес с каждой тренировкой❗️ Выполняем 15 повторений❗️\n\n3. <b>Удержание</b>. Приседаем до положения, пока тело не станет паралельно земле, между ногами и телом угл 90 градусов❗️ Удерживаем эту позицию максимальное время❗️\n\n4. <b>Приседания + подъём на носках</b>. Приседаем, затем в верхней позиции делаем подъём на носках. Стараемся делать упражнение как можно медленее, 4-5 секунд опускания вниз и 3-4 подъёма вверх❗️ Выполняем упражнение на максимум❗️\n\n5. <b>Голень</b>. Берём какой-то предмет 10-15 см в высоту, на котором удобно стоять. Становимся возле стены и упираем руки, ставим носок 1 ноги на край премета, пятка должна быть ниже носка и почти дотрагиваться пола, с это положения выжимаем себя 1 ногой, затем медленно опускаемся в исходное положение и повторяем❗️ Выполняем 20 повторений на каждую ногу❗️\n\nВыполняем 3 подхода в каждом упражнении, отдых между подходами 90 секунд❗️ В скором будущем выйдут новые уровни тренировки❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка ног LvL 3</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazapress1':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Скручивания</b>. Выполняем 20 повторений❗️\n\n2. <b>Планка</b>. Стоим на локтях❗️ Держим 30 секунд❗️\n\n3. <b>Удержание ног</b>. Ложимся на спину и поднимаем прямые ноги на угл 45 градусов❗️ Держим 30 секунд❗️\n\n4. <b>Велосипед</b>. Выполняем 20 повторений❗️\n\nВыполняем 2 подхода в каждом упражнении, отдых между подходами 60 секунд❗️ Между упражнения работаем без отдыха❗️\n\nЕсли получилось сделать все повторения в каждом🚀 из подходов, то переходим на LvL 2❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка пресса LvL 1</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazapress2':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Подъёмы + скручивания</b>. Ложимся на спину и поднимаем ноги, пока она не станут перпендикулярны полу, затем 3 раза тянимся до носков руками, при этом напргая пресс❗️ Ноги желательно держать прямыми❗️ Выполняем на максимум 1 подход❗️\n\n2. <b>Круговые движения ногами</b>. Ложимся на спину и делаем круговые обороты прямыми ногами❗️ Делаем по 15 оборотов в каждую сторону❗️ 3 подхода❗️\n\n3. <b>Велосипед</b>. Выполняем 2 подхода по 30 повторений❗️ Последний делаем на максимум❗️\n\nМежду упражнения отдых 60 секунд❗️ Не спешим, делаем упражнения не на скорость, при каждом повторении максимально напрягаем пресс❗️\n\nЕсли получилось сделать все повторения в каждом🚀 из подходов, то переходим на LvL 3❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка пресса LvL 2</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'bazapress3':
                bot.send_message(call.message.chat.id,
                                 'Начнём тренировку❗️\n\n1. <b>Круговые движения ногами</b>. Ложимся на спину и делаем круговые обороты прямыми ногами❗️ Делаем по 30 оборотов в каждую сторону без отдыха, то есть в сумме 60 кругом❗️ Да, это жёстко❗️ Нет, я не офигел❗️\n\nЕсли не получилось сделать, то выполняем тренировку LvL 2 и пытаемся выполнить LvL 3 через пару дней❗️\n\nВ скором будущем выйдут новые уровни тренировки❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Тренеровка пресса LvL 3</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'pushups':
                bot.send_message(call.message.chat.id,
                                 '<b>Отжимания</b>, правильная техника:\n\n1. Руки на ширине плеч, ноги вместе❗️ \n\n2. Закручиваем кисти немного внутрь, при опускании кисти и грудные мышцы должны быть на одном уровне❗️\n\n3. Во время движения пресс напряжён, поясница не провисает❗️ Держим всё тело в напряжении❗️ \n\n4. При опускании вниз вдох, при подъёме резкий выдох❗️\n\n5. Опускаемся вниз до касания грудью пола, поднимаеся до полного распрямления рук в локтях. В вверхней точке прожимаем, сокращая при это грудные мышцы❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Push-ups</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'pullups':
                bot.send_message(call.message.chat.id,
                                 '',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Pull-ups</b>:", parse_mode='html',
                                      reply_markup=None)
            elif call.data == 'sklepka1':
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
                                 'Новый день - новый <b>Challenge</b>. Становимся в позицию отжиманий и опускаем локти на пол❗️ Пытаемся выжаться с этой позиции в позицию на прямых руках. \n\nПрокачайся🚀 за карантин❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Daily Challenge</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'week1':
                bot.send_message(call.message.chat.id,
                                 'Challenge на неделю -  увеличь отжимания на 10❗️\n\nЕсли ещё не тренировал грудь или трицепс сегодня, то проверь свой максимум в отжиманиях. Далее, перейди в раздел <b>База</b> и выбери <b>Push</b>❗️ Поставь себе за цель до конца недели увеличть количевство отжиманий на 10, выполняя тренировку <b>Push</b> через день или 2, если необходимо дополнительное восстановление❗️\n\nУдачи, у тебя целая неделя, что бы затащить❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Weekly Challenge</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'new':
                bot.send_message(call.message.chat.id,
                                 'Front Lever <b>Level 1</b>.\n\nСначала разберёмся с техникой. Руки всегда прямые, стараемся избегать сгибаний в локтях. При идеальной форме тело должно идти одной линией, без прогибов в пояснице, лопатки сведены.\n\nТеперь перейдём к тренировке.\n\n1. Подтягивания 5-10 повторений 4 подхода.\n\n2. Сведение лопаток, висим на турнике и сводим лопатки вертикальным движением корпуса вверх, 10-15 повторений на 3 подхода.\n\n3. Ноги к перекладине. С положения виса на турнике поднимает ноги и пытаемся коснутся носками турника 3 подхода по 8 повторений.\n\n4. С положения виса на турнике сгибаем ноги в коленях и подводим к пресу, удерживаем 15-20 секунд на 4 подхода.',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Front Lever</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'inter':
                bot.send_message(call.message.chat.id,
                                 'Front Lever <b>Level 2</b>.\n\n0. Начнём с попыток. Для начала пробуем держать передний вис, 10-15 попыток\n\n1. Поднимаем колени к груди и занимаем позицию переднего виса, выпрямляем ноги и опускаемся максимально медленно. Повторяем 10-15 раз.\n\n2. Поднимаем колени к груди и принимаем положение переднего виса. Держим такую позицию 20 секунд.\n\n3. Подтягивания в уголке 3-8 раз.\n\n4. Носки к турнику 10-15 повторений.\n\n5. С положения виса сводим лопатки и пытаемся приподнять корпус, 10 повторений.\n\nДелаем 2 таких круга, отдых между всеми упражнениями 90 секунд.',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Front Lever</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'new1':
                bot.send_message(call.message.chat.id,
                                 'Planche <b>Level 1</b>.\n\nДля начала разберёмся с правильной формой.\n1. При планше руки должны быть прямые, без сгибаний в локтях.\n\n2. Лопатки разведены, создаём небольшой горб на спине.\n\n3. Взгляд направлен вперёд.\n\nhttps://www.youtube.com/watch?v=POq_-CTIX3o&t=263s',
                                 parse_mode='html')
                bot.send_message(call.message.chat.id,
                                 'Теперь можно начать тренировку.\n\n1. Занимаем положение упор лёжа и пытаемся накатитя плечами максимально вперёд, делаем отжимания 3 подхода на 1-2 повторений.\n\n2. Накатываем плечи вперёд и удерживаем положение максимальное время на 3 подхода.\n\n3. Накаты плечами вперёд, как можно дальше, из положения упора лёжа, затем возвращаемся в стартовое положение, 10 раз.\n\n4. Становимся на колени и повторяем предыдущее упражнение с колен.\n\n\nВсегда следи, что бы руки были прямыми❗️\n\nДелаем таких 2 круга❗️ После первого круга отдых 2 минуты❗️ Отдых 60-90 секунд между упражнениями❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Planche</b>:", parse_mode='html',
                                      reply_markup=None)

            elif call.data == 'inter1':
                bot.send_message(call.message.chat.id,
                                 'Planche <b>Level 2</b>.\n\nНачнём тренировку❗️\n\n0. Перед началом попробуем сделать планш, 5-8 попыток.\n\n1. Накатываемся плечами вперёд, поднимаем таз и пытаемся подойти ногами как можно ближе к рукам, возвращаемся в исходное положение, 3 подхода на 7-10 повторений.\n\n2. Накатываем плечи вперёд и делаем 5-7 отжиманий на 4 подхода.\n\n3. Накатываем плечи и держим 20-30 секунд.\n\nДелаем 2 таких круга, после чего делаем упражнение №4.\n\n4. Ставим руки по шире и накатываем плечи вперёд, держим на максимум 5 раз.\n\nВсегда следите за прямыми руками❗️ Отдых между кругами 2 минуты❗️',
                                 parse_mode='html')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Учим Planche</b>:", parse_mode='html',
                                      reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

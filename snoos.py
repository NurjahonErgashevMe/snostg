import subprocess
import sys


def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Устанавливаем {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install_and_import("random")
install_and_import("string")
install_and_import("smtplib")
install_and_import("email")
install_and_import("time")

# Теперь можно использовать библиотеки
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

access_codes = ["admin"]

# Отправители и их пароли
senders = {
    # 'lyimbshsup@rambler.ru': '6463734rnAygg',
    #        'jdqukazixk@rambler.ru': '0225223ACFeq0',
    #        'baljufgcnc@rambler.ru': '4738678YMyCvO',
    #        'ruslanorlovimx4134@rambler.ru': 'Andersonnancy945',
    #        'vladislavkulikovxcr1902@rambler.ru': 'Allenkimberly021',
    #        'romasidorovdbj3700@rambler.ru': 'Clarkmargaret444',
    #        'lehabogdanovhdw1954@rambler.ru': 'Evanssandra913',
    #        'mihailtitovopr6182@rambler.ru': 'Younghelen407',
    #        'koljafedotovmqj2347@rambler.ru': 'Gonzalezsarah321',
    #        'genasemenovhvu9785@rambler.ru': 'Taylorlaura482',
    #        'vovafedorovmvu7067@rambler.ru': 'Collinsbetty976',
    #        'grishakulikovyyk8848@rambler.ru': 'Wilsonlaura931',
    #        'olegnikitinxwo3553@rambler.ru': 'Wrightkaren568',
    #        'gennadijkalininizb3132@rambler.ru': 'Turnerdorothy038',
    #        'bogdankarpovxad9304@rambler.ru': 'Carterlinda019',
    "koljakuznecovzfq8892@rambler.ru": "Walkerhelen225",
    "vladdmitrievtpv8734@rambler.ru": "Brownmary434",
    "arturkovalevdln7432@rambler.ru": "Lewisnancy365",
    "konstantinbelovabq7348@rambler.ru": "Allenmary923",
    "sashavorobevbml8362@rambler.ru": "Hilllaura818",
    "ruslankozlovhji7240@rambler.ru": "Hallnancy735",
    "olegzajcevepy8163@rambler.ru": "Nelsonsharon117",
    "grigorijfominlxp0053@rambler.ru": "Wrightpatricia686",
    "vitalijmaslovusv3737@rambler.ru": "Garciabetty827",
    "olegbelovblx5518@rambler.ru": "Phillipssharon437",
    "olegmaslovrde8926@rambler.ru": "Mitchellbetty324",
    "vitalijdavydovtal6583@rambler.ru": "Rodriguezmichelle351",
    "dmitrijmironovlaf9788@rambler.ru": "Whitedeborah816",
    "vanjakulikovdpf6394@rambler.ru": "Allencarol017",
    "andrejmaksimovwjw5202@rambler.ru": "Cartersusan436",
    "zhenjaafanasevomj8876@rambler.ru": "Harrislinda730",
    "sanjatimofeevxur1820@rambler.ru": "Martinmichelle433",
    "grishabogdanovhqj9645@rambler.ru": "Turnermargaret062",
    "viktorpavlovzlh2404@rambler.ru": "Hilllaura917",
    "mihailkuznecovbuh2424@rambler.ru": "Millerkaren783",
    "bogdanmironovkgf3690@rambler.ru": "Greenjennifer095",
    "tolikkulikovnfv3662@rambler.ru": "Perezelizabeth881",
    "sanjaabramovotb8410@rambler.ru": "Hillpatricia526",
    "pashabykovzhy8581@rambler.ru": "Scottdonna750",
    "jurijbogdanovwuc0744@rambler.ru": "Harrisnancy027",
    "antongusevaws0670@rambler.ru": "Collinsruth779",
    "maksimlebedevsxm5444@rambler.ru": "Evanskaren499",
    "vladimirchernyshevfnt3789@rambler.ru": "Halldonna541",
    "petjagusevrzl9637@rambler.ru": "Taylorpatricia485",
    "vitaliklebedevhla3289@rambler.ru": "Lewismichelle721",
    "aleksandrwerbakovsbg8385@rambler.ru": "Gonzalezdeborah554",
    "pavelgrigorevjtz4407@rambler.ru": "Campbellbetty034",
    "maksdenisovskv0461@rambler.ru": "Smithmaria151",
    "gennadijtihonovqzc3691@rambler.ru": "Clarksharon602",
    "ruslandmitrievvgr1236@rambler.ru": "Kingdeborah697",
    "genamaslovfys4433@rambler.ru": "Wrightsharon746",
    "borjamironovfrc3345@rambler.ru": "Harrissusan337",
    "antonchernovown4062@rambler.ru": "Thomaskimberly712",
    "vladimirgrigoreveqq9112@rambler.ru": "Parkermichelle304",
    "sashawerbakoviet2953@rambler.ru": "Clarksharon806",
    "mishaantonovcwv6881@rambler.ru": "Kingmargaret388",
    "mihailmelnikovoyp1458@rambler.ru": "Wilsonlisa429",
    "kostjakiselevhjw4194@rambler.ru": "Evanshelen904",
    "kostjastepanovbes5317@rambler.ru": "Carterlaura187",
    "toljadanilovcvh2967@rambler.ru": "Martinezbarbara968",
    "leshakozlovspt3407@rambler.ru": "Hernandezbetty901",
    "vanjakozlovbvy7090@rambler.ru": "Jonescarol966",
    "leshafilippovfha9160@rambler.ru": "Davislinda702",
    "olegjakovlevmkp6120@rambler.ru": "Perezjennifer226",
    "igorisaevfen3865@rambler.ru": "Allenpatricia615",
    "pashakonovalovgmf3693@rambler.ru": "Garciamichelle737",
    "vladimirandreevqol3763@rambler.ru": "Robinsonkimberly357",
    "jurijprohorovgnq3561@rambler.ru": "Kinglaura374",
    "vladislavtarasovpqk4498@rambler.ru": "Garciacarol344",
    "antonvorobevtxz5033@rambler.ru": "Lopezlinda159",
    "romaandreevjvo1698@rambler.ru": "Youngnancy376",
    "vladislavbeljaevvfa7045@rambler.ru": "Robertsjennifer080",
    "vitaliknikolaevzoh1565@rambler.ru": "Collinsdonna967",
    "koljamironovydt4703@rambler.ru": "Wrightmichelle859",
    "gennadijsemenovmki9018@rambler.ru": "Perezsusan734",
    "pashakarpovafr2420@rambler.ru": "Wrightsarah462",
    "artemkomarovqqt3719@rambler.ru": "Martinlinda992",
    "konstantinchernyshevneh8321@rambler.ru": "Smithdonna021",
    "grigorijsidorovrpl5056@rambler.ru": "Harrispatricia221",
    "petrsergeevmse2216@rambler.ru": "Bakerjennifer796",
}


receivers = [
    "sms@telegram.org",
    "dmca@telegram.org",
    "abuse@telegram.org",
    "support@telegram.org",
]


def print_logo():
    print(""" 

        HELLO WORLD

        """)


def print_menu():
    print("\033[92mМеню:\033[0m")
    print("[ 1 ] Snos аккаунта")
    print("[ 2 ] Snos канала")
    print("[ 3 ] Меню\n")


def send_email(receiver, sender_email, sender_password, subject, body):
    for sender_email, sender_password in senders.items():
        try:
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP("smtp.rambler.ru", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)
            server.quit()
            return True
        except Exception:
            continue
    return False


def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0

    while sent_emails < total_emails:
        print_logo()
        print_menu()
        choice = input("\nВыбор: ")

        if choice == "1":
            print("\nВыберите тип жалобы:")
            print("\n[ 1.1 ] Обычный snos")
            print("[ 1.2 ] snos сеsсий")
            complaint_choice = input("Ваш выбор: ")

            if complaint_choice == "1.1":
                print(
                    "\nВведите причину, юзернейм, telegram ID, затем ссылки на канал/чат и на нарушение"
                )
                reason = input("\nПричина: ")
                username = input("Юзернейм: ")
                telegram_ID = input("Telegram ID: ")
                chat_link = input("\n\nСсылка на чат: ")
                violation_chat_link = input("\nСсылка на нарушение: ")

                complaint_texts = {
                    "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(
                            reason=reason.strip(),
                            username=username.strip(),
                            telegram_ID=telegram_ID.strip(),
                            chat_link=chat_link.strip(),
                            violation_chat_link=violation_chat_link.strip(),
                        )
                        send_email(
                            receiver_email,
                            sender_email,
                            sender_password,
                            "Жалоба на Telegram аккаунт",
                            complaint_body,
                        )
                        print(
                            f"\n\n[ Удачно ] Жалоба отправлена! | {receiver_email} от {sender_email}!"
                        )
                        sent_emails += 1

            elif complaint_choice == "1.2":
                print("\nВведите юзернейм и Telegram ID")
                account_username = input("\nUsername: ")
                Telegram_account_ID = input("Telegram ID: ")

                complaint_texts = {
                    "1.2": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {account_username}, а мой айди, если злоумышленник поменял юзернейм — {Telegram_account_ID}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(
                            account_username=account_username.strip(),
                            Telegram_account_ID=Telegram_account_ID.strip(),
                        )
                        send_email(
                            receiver_email,
                            sender_email,
                            sender_password,
                            "Я утерял свой телеграм-аккаунт",
                            complaint_body,
                        )
                        print(
                            f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email} от {sender_email}!"
                        )

        elif choice == "2":
            print("\nВыберите тип жалобы:")
            print("\n\n[ 8 ] Личные данные")
            print("[ 9 ] Для прайсов")
            print("[ 10 ] Для геймов")
            print("[ 11 ] Детское питание")
            print("[ 12 ] Мошенничество")
            print("[ 13 ] Продажа вирт номеров")
            print("[ 14 ] Расчлененка")
            print("[ 15 ] Живодерство")
            complaint_type = input("\nВыбор: ")

            complaint_types = {
                "8": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются личные данные невинных людей. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform",
                ],
                "9": [
                    "Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{violation_link} Просьба заблокировать данный канал.",
                    "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel.",
                ],
                "10": [
                    "Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance",
                    "Здравствуйте, уважаемая поддержка Telegram! Пожалуйста, заблокируйте канал {channel_link}. В этом канале угрожают расстрелом детей в школах и совершением террористических актов, вы можете увидеть это здесь {violation_link}. Заранее спасибо.",
                ],
                "11": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуется порнография с несовершеннолетними детьми. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel",
                ],
                "12": [
                    "Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются посты с целью обмана и мошенничества. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки",
                    "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform.",
                ],
                "13": [
                    "Здравствуйте, поддержка telegram. Я бы хотел пожаловаться на телеграм канал продающий виртуальные номера, насколько я знаю это запрещено правилами вашей площадки. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link} . Спасибо что очищаете свою площадку от подобных каналов!",
                    "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!",
                ],
                "14": [
                    "Доброго времени суток, уважаемая поддержка. На просторах вашей платформы мне попался канал, распространяющий шок контент с убийствами людей. Ссылка на канал - {channel_link} , ссылка на нарушение - {violation_link} . Просьба удалить данный канал, спасибо за внимание.",
                    "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention.",
                ],
                "15": [
                    "Здравствуйте, уважаемая поддержка. На вашей платформе я нашел канал который выкладывает жестокое обращение с животными. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link}. Спасибо за то что делаете телеграм чище.",
                    "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you",
                ],
            }

            if complaint_type not in complaint_types:
                print("\n\n[ Error ] Некорректный выбор.")
            else:
                complaint_texts = complaint_types[complaint_type]
                channel_link = input("\nСсылка на канал: ")
                violation_link = input("Ссылка на нарушение: ")

                for sender_email, sender_password in senders.items():
                    for receiver_email in random.sample(
                        receivers, min(2, len(receivers))
                    ):
                        complaint_body = complaint_texts[0].format(
                            channel_link=channel_link.strip(),
                            violation_link=violation_link.strip(),
                        )
                        send_email(
                            receiver_email,
                            sender_email,
                            sender_password,
                            "Жалоба на канал в Telegram",
                            complaint_body,
                        )
                        print(f"\n\n[ Удачно ] Жалоба отправлена! |{receiver_email}!")
                        sent_emails += 1
                # Отправка писем на английском
                if len(complaint_texts) > 1:
                    for sender_email, sender_password in senders.items():
                        for receiver_email in random.sample(
                            receivers, min(2, len(receivers))
                        ):
                            complaint_body = complaint_texts[1].format(
                                channel_link=channel_link.strip(),
                                violation_link=violation_link.strip(),
                            )
                            send_email(
                                receiver_email,
                                sender_email,
                                sender_password,
                                "Complaint about a channel in Telegram",
                                complaint_body,
                            )
                            print(f"Sent to {receiver_email}!")
                            sent_emails += 1
                print("[ Удачно ] Жалоба отправлена! |")

        elif choice == "5":
            print("Укажите свою почту для проверки работоспособности почт")
            test_email = input("Ваша почта: ")
            complaint_types = {
                "Тест": [
                    "Сейчас я отправлю на почту {test_email} письма с моих почт в качестве теста"
                ]
            }
            successfully_sent_emails = (
                0  # Переменная для отслеживания успешно отправленных писем
            )
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    for complaint_choice, complaint_texts in complaint_types.items():
                        complaint_text = complaint_texts[0]
                        complaint_body = complaint_text.format(
                            test_email=test_email.strip()
                        )
                        if send_email(
                            receiver_email,
                            sender_email,
                            sender_password,
                            "ТЕСТОВОЕ ПИСЬМО LOVE DELAINS",
                            complaint_body,
                        ):
                            successfully_sent_emails += 1
                            print(f"Отправлено на {receiver_email} от {sender_email}!")
                        else:
                            print(
                                f"Ошибка при отправке на {receiver_email} от {sender_email}!"
                            )
            print(f"Успешно отправлено {successfully_sent_emails} писем.")


def check_access_code():
    user_input = input("Введите код доступа: ")
    if user_input in access_codes:
        print("Код доступа верный. Программа запущена.")
        return True
    else:
        print("Неверный код доступа. Программа завершает работу.")
        return False


if __name__ == "__main__":
    if check_access_code():
        handle_complaint(senders, receivers)

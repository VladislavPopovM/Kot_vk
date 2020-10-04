import bs4, requests, random
class VKbot:
    def __init__(self, user_id):
        print("\nCreate BOT")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        
        self._COMMANDS = ["ПРИВЕТ","ПОКА","СПАСИБО","ДАЙ ПЕЧЕНЬКУ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]
    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        
        return result
    
    def get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    def new_message(self, message):
        #Hellow
        if (message.upper() == self._COMMANDS[0]):
            return f"Привет, {self._USERNAME}!"
        #Bye
        elif (message.upper() == self._COMMANDS[1]):
            return f"{self._USERNAME}, Пока(\nЖду твоего возвращения"
        #Tnx
        elif (message.upper() == self._COMMANDS[2]):
            return f"Обращайся, {self._USERNAME}!"
        elif (message.upper() == self._COMMANDS[3]):
            return f"Лови, {self._USERNAME}!"
        else :
            return "Я не понял тебя..."
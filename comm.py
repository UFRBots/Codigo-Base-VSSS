import paho.mqtt.client as mqtt
import time

"""
    mqtt_client = mqtt.Client("Dados dos Robos")
    mqtt_client.connect(host='localhost', port = 1883)
    mqtt_client.publish(topic="/messge", payload = "Dados do Robo")
"""


class RLCommMqttESQ:

    def __init__(self):
        self.__mqtt_client = None

    def start(self):
        mqttBroker = "192.168.0.101"
        print("Start communication esp ")
        self.__mqtt_client = mqtt.Client(client_id="Dados do robot para o esp")
        self.__mqtt_client.connect(host=mqttBroker)
        print("Ok! comm esp")

    def send_UFRBOTS(self, robot_commands=[]):
        # robo_2 = robot_commands[1]
        # message = f"({robo_2['robot_id']},{abs(robo_2['wheel_left'])},{abs(robo_2['wheel_right'])})"
        # self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=message)
        message = ""
        robot_commands = sorted(robot_commands, key=lambda i: i['robot_id'])
        for rb in robot_commands:
            # message += f"({rb['robot_id']},{abs(rb['wheel_left'])},{abs(rb['wheel_right'])})"
            
            # Goleiro
            if (rb['robot_id'] == 1):
                # Assim que começar a partida o goleiro vai virar na vertical
                self.__mqtt_client.publish(
                    topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['20'])},{abs(rb['0'])})")
                # A cada 4 segundos ele vai para frente ou para trás
                time.sleep(4)
                while (True):
                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['20'])},{abs(rb['20'])})")
                    
                    time.sleep(4)

                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['-20'])},{abs(rb['-20'])})")


            # Jogador 2 
            if (rb['robot_id'] == 2):
                # A cada 4 segundos ele vai para frente ou para trás
                time.sleep(4)
                while (True):
                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['20'])},{abs(rb['20'])})")
                    
                    time.sleep(4)

                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['-20'])},{abs(rb['-20'])})")

            
            # Jogador 3
            if (rb['robot_id'] == 3):
                # A cada 4 segundos ele vai para frente ou para trás
                time.sleep(4)
                while (True):
                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['20'])},{abs(rb['20'])})")
                    
                    time.sleep(4)

                    self.__mqtt_client.publish(
                        topic="UFRBots/transmit_robot", payload=f"({rb['1']},{abs(rb['-20'])},{abs(rb['-20'])})")


        # message = message[:-1] + ')'
        # print("Message:" + message)
        # self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=message)

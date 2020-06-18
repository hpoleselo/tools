#!/usr/bin/env python

import rospy


# falar rapidamente sobre o actionlib
import actionlib

# Mostrar estrutura da mensagem
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

client = 0

# Mostrar antes no rostopic a leitura e os respectivos nomes das juntas!!
nome_das_juntas = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']


# Queremos chegar no comportamento mostrado, como chegar?
# Basta pegar os valores das juntas em cada ponto, nesse caso nao vamos nos importar com a trajetoria



# rostopic echo -n1 /joint_states
# ir mexendo no TCP
config1 = [-1.4515393416034144, -1.556147877370016, -1.5984099547015589, -0.033115688954488576, 1.5721852779388428, -0.7098024527179163]
config2 =  [-1.9233949820147913, -1.7489426771747034, -1.3826277891742151, -0.061001125966207326, 2.0422892570495605, -0.7328742186175745]
config3 = [-1.9248164335833948, -1.9114554564105433, -0.6337674299823206, -0.6473959128009241, 2.043708562850952, -0.7329643408404749]
config4 = [-1.1509221235858362, -1.6764228979693812, -0.9353511969195765, -0.577367130910055, 1.2706621885299683, -0.6956394354449671]

# Entender quais bibliotecas sao necessarias para controlar o robo
# Entender o FollowJointTrajectoryGoal (dar motivacoes)

def mover_robo():
    # Instanciando um objeto novo chamado Objetivo
    objetivo = FollowJointTrajectoryGoal()

    # Mostrar estrutura da mensagem e o porque necessitamos atribuir os valores aos campos
    objetivo.trajectory = JointTrajectory()

    objetivo.trajectory.joint_names = nome_das_juntas
    objetivo.trajectory.points = [
        # as velocidades nao importam, apenas a posicao, portanto lista com 6 0s
        # rospy.Duration vai ditar o tempo para chegar naquela joint 
        JointTrajectoryPoint(positions=config1, velocities=[0]*6, time_from_start=rospy.Duration(2.0)),
        JointTrajectoryPoint(positions=config2, velocities=[0]*6, time_from_start=rospy.Duration(4.0)),
        # Falar sobre os tempos, que nao faz sentido colocar tempos extremamente baixos para configuracoes muito distantes no robo se nao
        # o solver de cinematica inversa vai calcular algo que nao faz sentido
        JointTrajectoryPoint(positions=config3, velocities=[0]*6, time_from_start=rospy.Duration(6.0)),
        JointTrajectoryPoint(positions=config4, velocities=[0]*6, time_from_start=rospy.Duration(8.0)),
        JointTrajectoryPoint(positions=config1, velocities=[0]*6, time_from_start=rospy.Duration(10.0))]

    client.send_goal(objetivo)
    try:
        client.wait_for_result()
    except(KeyboardInterrupt):
        client.cancel_goal()
        raise


def main():
    # Dar motivacao do porque separar em funcoes, falar que eh melhor usar como se fosse uma classe em Python (OO), mas nesse caso iremos trabalhar como funcoes basicas mesmo
    # Mas pra isso precisamos de uma variavel global
    global client
    try:
        # Disable signals pra poder funcionar os try/except de KeyBoard Interrupt
        rospy.init_node("teste_movimento", disable_signals=True)
        client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        print("Esperando o servidor...")
        client.wait_for_server()
        print("Conectado ao servidor")
        mover_robo()
    except(KeyboardInterrupt):
        rospy.signal_shutdown("Interrupcao do teclado")
        raise


if __name__ == "__main__":
    main()
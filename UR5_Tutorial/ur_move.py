import rospy

# Como queremos a interface com o robo, o pacote que indica isso eh o ur_driver (pesquisar no google para mostrar para os telespectadores)
import ur_driver

# falar rapidamente sobre o actionlib
import actionlib

# Mostrar estrutura da mensagem
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

client = 0

# Mostrar antes no rostopic a leitura e os respectivos nomes das juntas!!
nome_das_juntas = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

config1 = [0,0,0,0,0,0]
config2 = [1.57, 1.57, 1.57, 1.57, 1.57, 1.57]

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
        JointTrajectoryPoint(positions=config1, velocities=[0]*6, time_from_start=rospy.Duration(2.0))]
        #JointTrajectoryPoint(positions=config2, velocities=[0]*6, time_from_start=rospy.Duration(3.0))]
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
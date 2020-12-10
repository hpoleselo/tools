# CAN Networks

## Initial Concepts
ECU: Electronic Control Unit, modules are processing units have to transmit information between each other in order to *actuate*.
We can condense everything in one bus, making cheaper to traffic all the information in one cable and not passing cable through the whole system, like full-duplex.

node = module

There's no master or slave, is a bus (barramento) where each ECU can retrieve or send information on this bus.
The information is send through messages, message has its ID and its information (content), error, checksum from the protocol itself.
Dataframe is consisted of: 
X Bits bits = Error + Checksum + ID (in Hexadecimal) + Content (64 bits)
Inside of a message there're signals.

Where CAN is most common is in automotive industry, each car's subsystem has an . In order to diagnose the car or automate some tasks in your car we use the OBD2 connector, which has a CAN buses (HS1,HS2...) you cannot access ALL networks through OBD2, only a few points are accessed.

Each module has a CAN interface to talk with the network.

Networks with different bitrates can communicate with each other over a gateway ```GWM``` (like a router):
- HS1: HighSpeed1 500kbps
- HS2
- HS3
- MS: MediumSpeed 250kbytes/s
- LS: LowSpeed

All messages are published everytime, so we don't have to request or anything, just supply the ID and we're gonna get it.


## Notes

Hardware filters: masks that accept only certain IDs, for trigget-event messages, instead we lose a lot of processing for our system and bringing delay for our system. That's why the ID is the header of the message, because it makes quicker to filter it out, we don't have to read the whole message.

Para interconectar redes CAN usa-se um gateway.
Buzzload: muita informação, dividido em redes. Netconn team usually is responsible for that.

DBC: Database CAN, is like a dictionary for CAN. But why do we need it since we every message is sent over the CAN bus? It's useful **mainly** for the gateway component, because it HAS to know which message is going to be sent, so the the description ```DBC``` becomes important.
to other CAN network. 

DID variables: variables that can be changed/parametrized later (brightness, for example) even after the system is running. This is useful when
We can even update a module over CAN (has cryptography)

MDC: file, master which contains signals of all vehicles

Type of event: event (triggered), event and not periodic and fixed period.

## LIN
Some units use LIN instead of CAN, why? Because some information are restricted to one module (it doesn't have the need to send over the network, will be used
strictly by this module).
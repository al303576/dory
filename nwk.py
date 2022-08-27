class NWK():

    class FRAME_CONTROL():
        """ value is a string i.e '0x1208'  or a int i.e 235 """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.fcf == 0x{self.value:04x}'
            else:
                return f'zbee_nwk.fcf == {self.value}'

        class FRAME_TYPE():
            DATA = f'zbee_nwk.frame_type == 0x0'
            COMMAND = f'zbee_nwk.frame_type == 0x1'

            def __init__(self, frame_type):
                self.frame_type = frame_type

            def __str__(self):
                return f'zbee_nwk.frame_type == 0x{self.frame_type:x}'

        class PROTOCOL_VERSION():
            ZIGBEE_2007 = f'zbee_nwk.proto_version == 0x0'
            ZIGBEE_2006 = f'zbee_nwk.proto_version == 0x1'
            ZIGBEE_PRO = f'zbee_nwk.proto_version == 0x2'

            def __init__(self, protocol_version):
                self.protocol_version = protocol_version

            def __str__(self):
                return f'zbee_nwk.proto_version == 0x{self.protocol_version:x}'

        class DISCOVER_ROUTE():
            TRUE = f'zbee_nwk.discovery == 0x1'
            FALSE = f'zbee_nwk.discovery == 0x0'

            def __init__(self, discover_route):
                self.discover_route = discover_route

            def __str__(self):
                return f'zbee_nwk.discovery == 0x{self.discover_route:x}'

        class MULTICAST():
            TRUE = f'zbee_nwk.multicast == 0x1'
            FALSE = f'zbee_nwk.multicast == 0x0'

            def __init__(self, multicast):
                self.multicast = multicast

            def __str__(self):
                return f'zbee_nwk.multicast == 0x{self.multicast:x}'

        class SECURITY():
            TRUE = f'zbee_nwk.security == 0x1'
            FALSE = f'zbee_nwk.security == 0x0'

            def __init__(self, security):
                self.security = security

            def __str__(self):
                return f'zbee_nwk.security == 0x{self.security:x}'

        class SOURCE_ROUTE():
            TRUE = f'zbee_nwk.src_route == 0x1'
            FALSE = f'zbee_nwk.src_route == 0x0'

            def __init__(self, source_route):
                self.source_route = source_route

            def __str__(self):
                return f'zbee_nwk.src_route == 0x{self.source_route:x}'

        class DESTINATION_IEEE():
            TRUE = f'zbee_nwk.ext_dst == 0x1'
            FALSE = f'zbee_nwk.ext_dst == 0x0'

            def __init__(self, destination_ieee):
                self.destination_ieee = destination_ieee

            def __str__(self):
                return f'zbee_nwk.ext_dst == 0x{self.destination_ieee:x}'

        class EXTENDED_SOURCE():
            TRUE = f'zbee_nwk.ext_src == 0x1'
            FALSE = f'zbee_nwk.ext_src == 0x0'

            def __init__(self, extended_source):
                self.extended_source = extended_source

            def __str__(self):
                return f'zbee_nwk.ext_src == 0x{self.extended_source:x}'

        class END_DEVICE_INITS():
            TRUE = f'zbee_nwk.end_device_initiator == 0x1'
            FALSE = f'zbee_nwk.end_device_initiator == 0x0'

            def __init__(self, end_device_inits):
                self.end_device_inits = end_device_inits

            def __str__(self):
                return f'zbee_nwk.end_device_initiator == 0x{self.end_device_inits:x}'

    class DESTINATION_ADDRESS():
        """ value is a string i.e '0x1208'  or a int i.e 235 """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.dst == 0x{self.value:04x}'
            else:
                return f'zbee_nwk.dst == {self.value}'

    class SOURCE_ADDRESS():
        """ value is a string i.e '0x1208'  or a int i.e 235 """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.src == 0x{self.value:04x}'
            else:
                return f'zbee_nwk.src == {self.value}'

    class RADIUS():
        """ value is a string i.e '0x1208'  or a int i.e 235 """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.radius == 0x{self.value:02x}'
            else:
                return f'zbee_nwk.radius == {self.value}'

    class SEQUENCE_NUMBER():
        """ value is a string i.e '0x12'  or a int i.e 235 """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.seqno == 0x{self.value:x}'
            else:
                return f'zbee_nwk.seqno == {self.value}'

    class DESTINATION_EXTEND():

        def __init__(self, address):
            self.address = address

        def __str__(self):

            if type(self.address) == int:
                "convert address to string in the format 00:00:00:00:00:00:00:04"
                "insert ':' every 2 characters"
                address = f'{self.address:016x}'
                address = ':'.join([address[i:i+2]
                                    for i in range(0, len(address), 2)])
                return f'zbee_nwk.dst64 == {address}'
            else:
                return f'zbee_nwk.dst64 == {self.address}'

    class SOURCE_EXTEND():

        def __init__(self, address):
            self.address = address

        def __str__(self):

            if type(self.address) == int:
                "convert address to string in the format 00:00:00:00:00:00:00:04"
                "insert ':' every 2 characters"
                address = f'{self.address:016x}'
                address = ':'.join([address[i:i+2]
                                    for i in range(0, len(address), 2)])
                return f'zbee_nwk.src64 == {address}'
            else:
                return f'zbee_nwk.src64 == {self.address}'

    class SECURITY_HEADER():
    
        class SECURITY_CONTROL():
            """ value is a string i.e '0x12'  or a int i.e 235 """

            def __init__(self, value):
                self.value = value

            def __str__(self):
                if type(self.value) is int:
                    return f'zbee.sec.field == 0x{self.value:x}'
                else:
                    return f'zbee.sec.field == {self.value}'
        
        class FRAME_COUNTER():
            """ value is a string i.e '0x12'  or a int i.e 235 """

            def __init__(self, value):
                self.value = value

            def __str__(self):
                if type(self.value) is int:
                    return f'zbee.sec.counter == 0x{self.value:x}'
                else:
                    return f'zbee.sec.counter == {self.value}'
        
        class EXTENDED_SRC():
            def __init__(self, address):
                self.address = address

            def __str__(self):

                if type(self.address) == int:
                    "convert address to string in the format 00:00:00:00:00:00:00:04"
                    "insert ':' every 2 characters"
                    address = f'{self.address:016x}'
                    address = ':'.join([address[i:i+2]
                                        for i in range(0, len(address), 2)])
                    return f'zbee.sec.src64 == {address}'
                else:
                    return f'zbee.sec.src64 == {self.address}'
        
        class KEY_SEQUENCE_NUMBER():
            """ value is a string i.e '0x12'  or a int i.e 235 """

            def __init__(self, value):
                self.value = value

            def __str__(self):
                if type(self.value) is int:
                    return f'zbee.sec.key_seqno == 0x{self.value:x}'
                else:
                    return f'zbee.sec.key_seqno == {self.value}'

        class MIC():
            """ value is a string i.e '00:00:00:00'  or a int i.e 235 or 0x12131290 """

            def __init__(self, value):
                self.value = value

            def __str__(self):
    
                if type(self.value) == int:
                    "convert value to string in the format 00:00:00:00"
                    "insert ':' every 2 characters"
                    value = f'{self.value:08x}'
                    value = ':'.join([value[i:i+2]
                                        for i in range(0, len(value), 2)])
                    return f'zbee.sec.mic  == {value}'
                else:
                    return f'zbee.sec.mic  == {self.value}'

    class COMMAND():
        """ value is a string i.e '0x12'  or a int i.e 235 """

        ROUTE_REQUEST = 'zbee_nwk.cmd.id  == 0x01'
        ROUTE_REPLY = 'zbee_nwk.cmd.id  == 0x02'
        NETWORK_STATUS = 'zbee_nwk.cmd.id  == 0x03'
        LEAVE = 'zbee_nwk.cmd.id  == 0x04'
        ROUTE_RECORD = 'zbee_nwk.cmd.id  == 0x05'
        REJOIN_REQUEST = 'zbee_nwk.cmd.id  == 0x06'
        REJOIN_RESPONSE = 'zbee_nwk.cmd.id  == 0x07'
        LINK_STATUS = 'zbee_nwk.cmd.id  == 0x08'
        NETWORK_REPORT = 'zbee_nwk.cmd.id  == 0x09'
        NETWORK_UPDATE = 'zbee_nwk.cmd.id  == 0x0a'


        def __init__(self, value):
            self.value = value

        def __str__(self):
            if type(self.value) is int:
                return f'zbee_nwk.cmd.id  == 0x{self.value:x}'
            else:
                return f'zbee_nwk.cmd.id  == {self.value}'
        
        
class MAC():

    class FRAME_CONTROL():

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'wpan.fcf == 0x{self.value:04x}'

        class FRAME_TYPE():
            DATA_BEACON = f'wpan.frame_type == 0x0'
            DATA = f'wpan.frame_type == 0x1'
            ACK = f'wpan.frame_type == 0x2'
            MAC_CMD = f'wpan.frame_type == 0x3'

            def __init__(self, frame_type):
                self.frame_type = frame_type

            def __str__(self):
                return f'wpan.frame_type == 0x{self.frame_type:x}'

        class SECURITY_ENABLED():
            TRUE = f'wpan.security == 0x1'
            FALSE = f'wpan.security == 0x0'

            def __init__(self, security_enabled):
                self.security_enabled = security_enabled
            
            def __str__(self):
                return f'wpan.security == 0x{self.security_enabled:x}'

        class FRAME_PENDING():
            TRUE = f'wpan.frame_pending == 0x1'
            FALSE = f'wpan.frame_pending == 0x0'
        
            def __init__(self, frame_pending):
                self.frame_pending = frame_pending
            
            def __str__(self):
                return f'wpan.frame_pending == 0x{self.frame_pending:x}'

        class ACK_REQUEST():
            TRUE = f'wpan.ack_request == 0x1'
            FALSE = f'wpan.ack_request == 0x0'
        
            def __init__(self, ack_request):
                self.ack_request = ack_request
            
            def __str__(self):
                return f'wpan.ack_request == 0x{self.ack_request:x}'

        class PAN_ID_COMPRESSION():
            TRUE = f'wpan.pan_id_compression == 0x1'
            FALSE = f'wpan.pan_id_compression == 0x0'

            def __init__(self, pan_id_compression):
                self.pan_id_compression = pan_id_compression
            
            def __str__(self):
                return f'wpan.pan_id_compression == 0x{self.pan_id_compression:x}'

        class SEQ_NUM_SUPPRESSION():
            TRUE = f'wpan.seqno_suppression == 0x1'
            FALSE = f'wpan.seqno_suppression == 0x0'
        
            def __init__(self, seq_num_suppression):
                self.seq_num_suppression = seq_num_suppression
            
            def __str__(self):
                return f'wpan.seqno_suppression == 0x{self.seq_num_suppression:x}'

        class IES_PRESENT():
            TRUE = f'wpan.ie_present == 0x1'
            FALSE = f'wpan.ie_present == 0x0'
        
            def __init__(self, ies_present):
                self.ies_present = ies_present
            
            def __str__(self):
                return f'wpan.ie_present == 0x{self.ies_present:x}'

        class DESTINATION_ADDRESSING_MODE():
            NONE = f'wpan.dst_addr_mode == 0x0'
            SHORT = f'wpan.dst_addr_mode == 0x2'
            EXTENDED = f'wpan.dst_addr_mode == 0x3'

            def __init__(self, dst_addr_mode):
                self.dst_addr_mode = dst_addr_mode
            
            def __str__(self):
                return f'wpan.dst_addr_mode == 0x{self.dst_addr_mode:x}'

        class FRAME_VERSION():
            IEEE_802_15_4_2003 = f'wpan.version == 0x0'
            IEEE_802_15_4_2006 = f'wpan.version == 0x1'
            IEEE_802_15_4_2015 = f'wpan.version == 0x2'

            def __init__(self, version):
                self.version = version
            
            def __str__(self):
                return f'wpan.version == 0x{self.version:x}'

        class SOURCE_ADDRESSING_MODE():
            NONE = f'wpan.src_addr_mode == 0x0'
            SHORT = f'wpan.src_addr_mode == 0x2'
            EXTENDED = f'wpan.src_addr_mode == 0x3'

            def __init__(self, src_addr_mode):
                self.src_addr_mode = src_addr_mode
            
            def __str__(self):
                return f'wpan.src_addr_mode == 0x{self.src_addr_mode:x}'

    class SEQUENCE_NUMBER():

        def __init__(self, seq_num):
            self.seq_num = seq_num

        def __str__(self):
            return f'wpan.seq_no == {self.seq_num}'

    class DESTINATION_PAN_ID():

        def __init__(self, pan_id):
            self.pan_id = pan_id

        def __str__(self):
            return f'wpan.dst_pan == 0x{self.pan_id:04x}'

    class DESTINATION_ADDRESS_SHOT():

        def __init__(self, address):
            self.address = address

        def __str__(self):
            return f'wpan.dst16 == 0x{self.address:04x}'

    class DESTINATION_ADDRESS_EXTEND():

        def __init__(self, address):
            self.address = address

        def __str__(self):

            if type(self.address) == int:
                "convert address to string in the format 00:00:00:00:00:00:00:04"
                "insert ':' every 2 characters"
                address = f'{self.address:016x}'
                address = ':'.join([address[i:i+2]
                                   for i in range(0, len(address), 2)])
                return f'wpan.dst64 == {address}'
            else:
                return f'wpan.dst64 == {self.address}'

    class SOURCE_ADDRESS_SHOT():

        def __init__(self, address):
            self.address = address

        def __str__(self):
            return f'wpan.src16 == 0x{self.address:04x}'

    class SOURCE_ADDRESS_EXTEND():

        def __init__(self, address):
            self.address = address

        def __str__(self):

            if type(self.address) == int:
                "convert address to string in the format 00:00:00:00:00:00:00:04"
                "insert ':' every 2 characters"
                address = f'{self.address:016x}'
                address = ':'.join([address[i:i+2]
                                   for i in range(0, len(address), 2)])
                return f'wpan.src64 == {address}'
            else:
                return f'wpan.src64 == {self.address}'

    class COMMAND_ID():
        ASSOCIATION_REQUEST = "wpan.cmd == 0x01"
        ASSOCIATION_RESPONSE = "wpan.cmd == 0x02"
        DATA_REQUEST = "wpan.cmd == 0x04"
        BEACON_REQUEST = "wpan.cmd == 0x07"

        def __init__(self, command_id):
            self.command_id = command_id

        def __str__(self):
            return f'wpan.cmd == 0x{self.command_id:02x}'

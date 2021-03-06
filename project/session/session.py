#! /usr/bin/python
# -*- coding: utf-8 -*-

class Session():
    """a class for session"""
    
    def __init__(self, request_num, response_num, sockets_set, pcap_container):
        """request_num: request http's pos in the http list
        response_num: response http's pos in the http list
        sockets_set: all sockets related to the session"""
        
        self.init_req_num = request_num
        self.init_response_num = response_num
        self.sockets_set = sockets_set
        self.http_list = []
        self.pcap_packet_list = []
        
        #get http_list  and pcap_packet_list
        cur = 0
        for msg in pcap_container.msg_list:
            sockets = ((msg["src_addr"], msg["src_port"]), ((msg["dst_addr"], msg["dst_port"])))
            if (sockets in sockets_set):
                self.http_list.append(cur)
            cur += 1
        for pcap_packet in pcap_container.pcap_packets:
            #skip the ip or ethernet packets
            if (pcap_packet.top_layer < 3):
                continue
            sockets = ((pcap_packet.ip.src, pcap_packet.tcp.src_port), (pcap_packet.ip.dst, pcap_packet.tcp.dst_port))
            if (sockets in sockets_set):
                self.pcap_packet_list.append(pcap_packet.pcap_num-1)
            
        #statistic data
        self.sp_delay = -1
        self.upstream_traffic = -1
        self.downstream_traffic = -1
        self.resouce_distribution = {
        "text_traffic" : 0, #sum of content len
        "image_traffic" : 0, 
        "multipart_traffic" : 0, 
        "application_traffic" : 0, 
        "message_traffic" : 0, 
        "audio_traffic" : 0, 
        "video_traffic" : 0, 
        "unknown_traffic" : 0, 
        
        "text_count" : 0,   
        "image_count" : 0, 
        "multipart_count" : 0, 
        "application_count" : 0, 
        "message_count" : 0, 
        "audio_count" : 0, 
        "video_count" : 0, 
        "unknown_count" : 0
        }
    
    def clear_statistics(self):
        """a method to clear all the statistics data"""
        
        self.sp_delay = -1
        self.upstream_traffic = -1
        self.downstream_traffic = -1
        self.resouce_distribution = {
        "text_traffic" : 0,
        "image_traffic" : 0, 
        "multipart_traffic" : 0, 
        "application_traffic" : 0, 
        "message_traffic" : 0, 
        "audio_traffic" : 0, 
        "video_traffic" : 0, 
        "unknown_traffic" : 0, 
        
        "text_count" : 0,   #sum of content len
        "image_count" : 0, 
        "multipart_count" : 0, 
        "application_count" : 0, 
        "message_count" : 0, 
        "audio_count" : 0, 
        "video_count" : 0, 
        "unknown_count" : 0
        }

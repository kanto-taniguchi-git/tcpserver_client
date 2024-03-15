#!/usr/bin/python3

import nmap                   # Nmapライブラリのインポート

scanner = nmap.PortScanner()  # インスタンスの作成
print('ようこそ、Nmapスキャナーへ')

ip_addr = input('スキャンしたいIPアドレスを入力してください: ')
print('入力されたIPアドレス: ', ip_addr)
type(ip_addr)

resp = input('''\n実行したいスキャンタイプを選択してください 
                1)Syn Ack Scan
                2)UDP Scan
                3)Comprehensive Scan
                ''')

print('選択されたスキャンタイプ: ', resp)

if resp == '1':
    print('Nmap Version: ', scanner.nmap_version())  # Nmapのバージョンを表示
    scanner.scan(ip_addr, '1-1024', '-v -sS')        # 1~1024をスキャン、-vは詳細表示、-sSはSyn Ack Scan
    print(scanner.scaninfo())                        # スキャンについての情報

    scan_data = scanner[ip_addr]
    hostnames = scan_data['hostnames']
    # ホスト名の取得
    for hostname_info in hostnames:
        print(f"Hostname: {hostname_info['name']}, Type: {hostname_info['type']}")
    # IPアドレスの取得
    ipv4_address = scan_data['addresses']['ipv4']
    print(f"IPv4 Address: {ipv4_address}")

    # ホストの状態
    host_status = scan_data['status']['state']
    host_reason = scan_data['status']['reason']
    print(f"Host Status: {host_status}, Reason: {host_reason}")
    print('IPアドレスステータス: ', scanner[ip_addr].state())  # スキャンしたIPアドレスのステータス

    print(scanner[ip_addr].all_protocols())                   # スキャンされたIPアドレスで検出されたプロトコル
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())     # スキャンされたIPアドレス開いているTCPポートのリストを表示

elif resp == '2':
    print('Nmap Version: ', scanner.nmap_version())  # Nmapのバージョンを表示
    scanner.scan(ip_addr, '1-1024', '-v -sU')        # 1~1024をスキャン、-vは詳細表示、-sUはUDP Scan
    print(scanner.scaninfo())                        # スキャンについての情報
    
    print('IPアドレスステータス: ', scanner[ip_addr].state())  # スキャンしたIPアドレスのステータス
    print(scanner[ip_addr].all_protocols())                   # スキャンされたIPアドレスで検出されたプロトコル
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())     # スキャンされたIPアドレス開いているUDPポートのリストを表示

elif resp == '3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    
    scan_data = scanner[ip_addr]
    print(scan_data)
    print('IPアドレスステータス: ', scanner[ip_addr].state())  # スキャンしたIPアドレスのステータス
    print(scanner[ip_addr].all_protocols())                   # スキャンされたIPアドレスで検出されたプロトコル
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())     # スキャンされたIPアドレス開いているTCPポートのリストを表示

else:
    print('オプションの番号を入力してください😘')
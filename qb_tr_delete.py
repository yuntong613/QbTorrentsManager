from qbittorrentapi import Client
import datetime


def check_tr_list(category, days=60, file_size=50):
    rm_hash = []
    rm_list = []
    print('*' * 10, category, '*' * 10)
    qbt_client = Client(host="192.168.0.4:8080", username='admin', password='adminadmin', SIMPLE_RESPONSES=True)
    list_tr = qbt_client.torrents_info(category=category)
    tm_now = datetime.datetime.now()
    for obj in list_tr:
        added_on = obj['added_on']
        last_activity = obj['last_activity']
        name = obj['name']
        total_size = obj['total_size']
        last_date = datetime.datetime.fromtimestamp(last_activity)
        if (tm_now - last_date).days >= days and total_size <= file_size * 1073741824:
            rm_list.append(name)
        else:
            if rm_list.count(name) > 0:
                rm_list.remove(name)
    for obj in list_tr:
        name = obj['name']
        tr_hash = obj['hash']
        if rm_list.count(name) > 0:
            rm_hash.append(tr_hash)
    print('name array:')
    print(rm_list)
    print('hash array:')
    print(rm_hash)
    if len(rm_hash) > 0:
        qbt_client.torrents_delete(delete_files=True, torrent_hashes=rm_hash)


if __name__ == '__main__':
    categories = ['movie', 'TV', 'Anime', 'xxx']
    for ca in categories:
        check_tr_list(ca)

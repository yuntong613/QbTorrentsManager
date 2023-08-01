from qbittorrentapi import Client
import datetime


def check_tr_list(old_tracker, new_tracker):
    qbt_client = Client(host="192.168.0.4:8080", username='admin', password='adminadmin', SIMPLE_RESPONSES=True)
    list_tr = qbt_client.torrents_info()
    hash_list = []
    for obj in list_tr:
        tr_hash = obj['hash']
        tracker_list = qbt_client.torrents_trackers(tr_hash)
        for tracker in tracker_list:
            tracker_url = tracker['url']
            if old_tracker in tracker_url:
                hash_list.append({'hash': tr_hash, 'tracker': tracker_url})

    for obj in hash_list:
        tr_hash = obj['hash']
        tr_tracker = obj['tracker']
        print(tr_hash, ',', tr_tracker, end='\n')
        qbt_client.torrents_edit_tracker(tr_hash, tr_tracker, new_tracker)


if __name__ == '__main__':
    old_tracker = 'hdarea.co'
    new_tracker = 'https://tracker.hdarea.club/announce.php?passkey=xxxxxx'
    check_tr_list(old_tracker, new_tracker)

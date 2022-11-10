import time
from datetime import datetime
from utils import DomainsSelector, UrlSelector, SelectorAccount
from google import Authorization, Indexing


def clear_accepted_urls(temp_urls, accepted_urls):
    for url in accepted_urls:
        temp_urls.remove(url)
    return temp_urls


def loop():
    print("Приложение запущено!")
    domain_selector = DomainsSelector.DomainSelector()
    account_selector = SelectorAccount.SelectAccount(domain_selector.get_all_accounts,
                                                     domain_selector.get_path_account_json)
    account = Authorization.Authorization(domain_selector.get_path_account_json)
    indexer = Indexing.Indexation(account)

    temp_links: list = list()
    try:
        while True:
            if len(temp_links) != 0:
                result = indexer.worker(temp_links, "URL_UPDATED")

                if result[0] is False:
                    account_selector.unvalid_account()
                    account.set_file_path(account_selector.get_valid_account)
                    indexer.set_account(account)
                    if not result[1].__eq__("google_error"):
                        print(f"{datetime.now().replace(microsecond=0)}. Google вернул квоту в 200 ссылок")
                    time.sleep(1)
                    accepted_links = indexer.get_accepted_urls
                    url_selector = UrlSelector.UrlSelector(delete_links=False)
                    url_selector.write_accepted_links(accepted_links)
                    indexer.clear_accepted_urls()
                    if len(accepted_links) != 0:
                        temp_links = clear_accepted_urls(temp_links, accepted_links)
                    else:
                        continue
                accepted_links = indexer.get_accepted_urls
                url_selector = UrlSelector.UrlSelector(delete_links=False)
                url_selector.write_accepted_links(accepted_links)
                indexer.clear_accepted_urls()
                if len(accepted_links) != 0:
                    temp_links = clear_accepted_urls(temp_links, accepted_links)

                else:

                    continue
            else:
                try:
                    url_selector = UrlSelector.UrlSelector(delete_links=True)
                except TypeError:
                    # Отсутствие ссылок в файле для ссылок
                    time.sleep(5)
                    continue
                temp_links = url_selector.get_links
                time.sleep(5)
                continue
    except KeyboardInterrupt:
        print("Дозапись неиспользованных ссылок")
        url_selector = UrlSelector.UrlSelector(delete_links=False)
        if len(temp_links) != 0:
            temp_links[0] = "\n" + temp_links[0]
        url_selector.overwriting_links(temp_links)


if __name__ == "__main__":
    loop()

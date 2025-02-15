# //enter file is a list of list of LU group by orders
#
# //function that as return gives ordered LU list

batch =[
 ["WAN-033529", "WAN-029114"],
 ["WAN-034972", "WAN-029372"],
 ["WAN-034972", "WAN-034315"],
 ["WAN-028898", "WAN-033210"],
 ["WAN-032114", "WAN-033529", "WAN-034315"],
 ["WAN-033468", "WAN-029372", "WAN-033210"],
 ["WAN-029372", "WAN-033210", "WAN-032597"],
 ["WAN-034972", "WAN-033682", "WAN-033210"],
 ["WAN-030741", "WAN-028940", "WAN-029372"],
 ["WAN-034660", "WAN-033468", "WAN-029558"],
 ["WAN-034958", "WAN-029558", "WAN-035266"],
 ["WAN-033682", "WAN-034958", "WAN-033529"],
 ["WAN-032776", "WAN-028898", "WAN-032597"],
 ["WAN-034958", "WAN-033529", "WAN-029188"],
 ["WAN-033682", "WAN-029372", "WAN-033210"],
 ["WAN-034972", "WAN-029188", "WAN-032776"],
 ["WAN-033682", "WAN-028940", "WAN-033210"],
 ["WAN-030882", "WAN-030817", "WAN-032597"],
 ["WAN-030882", "WAN-032405", "WAN-032597"],
 ["WAN-034972", "WAN-028898", "WAN-030817"],
 ["WAN-030882", "WAN-029188", "WAN-033210", "WAN-029114"],
 ["WAN-030741", "WAN-028940", "WAN-034633", "WAN-028898"],
 ["WAN-032405", "WAN-030817", "WAN-034315", "WAN-029114"],
 ["WAN-034660", "WAN-029372", "WAN-030817", "WAN-032597"],
 ["WAN-030741", "WAN-030882", "WAN-030817", "WAN-032597"],
 ["WAN-033468", "WAN-029188", "WAN-034633", "WAN-034315"],
 ["WAN-033529", "WAN-032776", "WAN-029558", "WAN-034315"],
 ["WAN-028940", "WAN-034958", "WAN-029188", "WAN-030817"],
 ["WAN-034958", "WAN-033529", "WAN-028898", "WAN-034315"],
 ["WAN-030741", "WAN-033468", "WAN-032405", "WAN-034958"],
 ["WAN-028940", "WAN-029372", "WAN-035266", "WAN-030817"],
 ["WAN-034660", "WAN-033529", "WAN-029188", "WAN-030817"],
 ["WAN-030741", "WAN-034958", "WAN-029558", "WAN-032597"],
 ["WAN-034972", "WAN-032776", "WAN-034633", "WAN-029114"],
 ["WAN-030741", "WAN-033529", "WAN-032776", "WAN-032597"],
 ["WAN-034972", "WAN-033529", "WAN-028898", "WAN-032597"],
 ["WAN-033468", "WAN-032405", "WAN-032776", "WAN-035266"],
 ["WAN-034633", "WAN-029558", "WAN-028898", "WAN-029114"],
 ["WAN-029372", "WAN-029558", "WAN-028898", "WAN-032597"],
 ["WAN-034660", "WAN-030741", "WAN-029188", "WAN-032776"],
 ["WAN-030741", "WAN-033468", "WAN-030882", "WAN-032405"],
 ["WAN-032776", "WAN-029372", "WAN-034633", "WAN-029558"],
 ["WAN-029188", "WAN-028898", "WAN-033210", "WAN-029114"],
 ["WAN-028940", "WAN-033529", "WAN-028898", "WAN-029114"],
 ["WAN-034660", "WAN-028940", "WAN-034633", "WAN-030817"],
 ["WAN-030882", "WAN-034958", "WAN-029372", "WAN-029114"],
 ["WAN-033468", "WAN-033529", "WAN-033210", "WAN-029114"],
 ["WAN-033682", "WAN-028940", "WAN-029188", "WAN-029114"],
 ["WAN-034958", "WAN-029558", "WAN-030817", "WAN-032597"],
 ["WAN-033468", "WAN-033529", "WAN-029558", "WAN-032597"],
 ["WAN-030882", "WAN-033529", "WAN-034633", "WAN-034315"],
 ["WAN-033468", "WAN-034958", "WAN-032776", "WAN-029558"],
 ["WAN-032114", "WAN-030882", "WAN-034633", "WAN-030817"],
 ["WAN-029188", "WAN-029558", "WAN-035266", "WAN-030817"],
 ["WAN-029558", "WAN-030817", "WAN-034315", "WAN-029114"],
 ["WAN-034972", "WAN-028898", "WAN-030817", "WAN-033210"],
 ["WAN-034660", "WAN-032776", "WAN-034633", "WAN-033210"],
 ["WAN-030741", "WAN-033468", "WAN-030882", "WAN-029558"],
 ["WAN-034958", "WAN-032776", "WAN-028898", "WAN-034315"],
 ["WAN-033468", "WAN-029188", "WAN-034633", "WAN-029558"],
 ["WAN-034660", "WAN-033529", "WAN-029188", "WAN-029372"],
 ["WAN-030741", "WAN-030882", "WAN-032405", "WAN-032597"],
 ["WAN-034958", "WAN-028898", "WAN-030817", "WAN-032597"],
 ["WAN-033468", "WAN-034633", "WAN-033210", "WAN-032597"],
 ["WAN-030741", "WAN-033468", "WAN-034633", "WAN-035266"],
 ["WAN-034958", "WAN-029372", "WAN-034315", "WAN-033210"],
 ["WAN-034972", "WAN-033468", "WAN-035266", "WAN-029114"],
 ["WAN-030882", "WAN-033529", "WAN-029372", "WAN-034315"],
 ["WAN-034660", "WAN-030882", "WAN-029372", "WAN-029114"],
 ["WAN-033529", "WAN-029188", "WAN-029372", "WAN-032597"],
 ["WAN-033682", "WAN-032405", "WAN-029372", "WAN-030817"],
 ["WAN-033682", "WAN-030882", "WAN-034633", "WAN-032597"],
 ["WAN-034972", "WAN-029558", "WAN-033210", "WAN-029114"],
 ["WAN-034660", "WAN-030882", "WAN-030817", "WAN-033210"],
 ["WAN-034660", "WAN-028940", "WAN-035266", "WAN-029114"],
 ["WAN-032405", "WAN-034958", "WAN-035266", "WAN-033210"],
 ["WAN-032114", "WAN-033468", "WAN-033529", "WAN-034633"],
 ["WAN-033468", "WAN-034958", "WAN-033529", "WAN-029188"],
 ["WAN-034972", "WAN-030741", "WAN-030882", "WAN-028898"],
 ["WAN-030741", "WAN-033468", "WAN-030882", "WAN-032776"],
 ["WAN-030882", "WAN-033529", "WAN-029372", "WAN-034633"],
 ["WAN-029372", "WAN-034315", "WAN-029114", "WAN-032597"],
 ["WAN-033468", "WAN-033529", "WAN-029372", "WAN-029114"],
 ["WAN-034972", "WAN-033682", "WAN-034958", "WAN-032776"],
 ["WAN-033468", "WAN-034633", "WAN-029558", "WAN-032597"],
 ["WAN-033468", "WAN-029558", "WAN-028898", "WAN-029114"],
 ["WAN-034660", "WAN-030741", "WAN-028940", "WAN-034958"],
 ["WAN-030741", "WAN-030882", "WAN-029188", "WAN-032776"],
 ["WAN-033468", "WAN-033529", "WAN-032776", "WAN-029114"],
 ["WAN-033468", "WAN-028940", "WAN-034633", "WAN-028898"],
 ["WAN-032114", "WAN-034958", "WAN-032776", "WAN-034315"],
 ["WAN-032405", "WAN-033529", "WAN-029114", "WAN-032597"],
 ["WAN-034660", "WAN-032405", "WAN-030817", "WAN-034315"],
 ["WAN-030882", "WAN-034958", "WAN-034633", "WAN-029558", "WAN-030817"],
 ["WAN-034972", "WAN-033468", "WAN-034633", "WAN-029558", "WAN-033210"],
 ["WAN-034972", "WAN-030882", "WAN-034633", "WAN-028898", "WAN-029114"],
 ["WAN-030741", "WAN-033682", "WAN-032405", "WAN-029558", "WAN-030817"],
 ["WAN-034972", "WAN-033682", "WAN-030817", "WAN-034315", "WAN-033210"],
 ["WAN-034660", "WAN-033682", "WAN-030882", "WAN-029114", "WAN-032597"],
 ["WAN-034972", "WAN-030741", "WAN-033468", "WAN-033682", "WAN-028898"],
 ["WAN-034972", "WAN-030741", "WAN-029372", "WAN-028898", "WAN-034315"],
 ["WAN-034972", "WAN-033682", "WAN-029372", "WAN-034633", "WAN-029114"],
 ["WAN-028940", "WAN-030882", "WAN-033529", "WAN-029558", "WAN-034315"],
 ["WAN-033682", "WAN-029372", "WAN-034315", "WAN-029114", "WAN-032597"],
 ["WAN-034972", "WAN-030882", "WAN-032405", "WAN-029372", "WAN-034633"],
 ["WAN-032776", "WAN-034633", "WAN-034315", "WAN-029114", "WAN-032597"],
 ["WAN-034972", "WAN-033468", "WAN-033529", "WAN-029188", "WAN-029558"],
 ["WAN-033468", "WAN-030882", "WAN-032776", "WAN-030817", "WAN-034315"],
 ["WAN-034972", "WAN-028940", "WAN-030882", "WAN-029558", "WAN-035266"],
 ["WAN-034972", "WAN-033468", "WAN-032405", "WAN-029188", "WAN-032597"],
 ["WAN-034972", "WAN-030741", "WAN-033468", "WAN-028898", "WAN-035266"],
 ["WAN-030882", "WAN-033529", "WAN-032776", "WAN-029372", "WAN-033210"],
 ["WAN-033682", "WAN-028940", "WAN-030882", "WAN-028898", "WAN-030817"],
 ["WAN-030882", "WAN-032405", "WAN-028898", "WAN-030817", "WAN-034315"],
 ["WAN-033682", "WAN-028940", "WAN-030882", "WAN-029372", "WAN-034315"],
 ["WAN-030882", "WAN-033529", "WAN-032776", "WAN-028898", "WAN-032597"],
 ["WAN-034660", "WAN-033682", "WAN-032405", "WAN-028898", "WAN-034315"],
 ["WAN-034958", "WAN-029188", "WAN-029558", "WAN-030817", "WAN-033210"],
 ["WAN-034660", "WAN-032405", "WAN-032776", "WAN-034315", "WAN-029114"],
 ["WAN-033468", "WAN-028940", "WAN-030882", "WAN-029558", "WAN-033210"],
 ["WAN-030741", "WAN-033468", "WAN-032405", "WAN-030817", "WAN-033210"],
 ["WAN-033682", "WAN-032776", "WAN-029558", "WAN-030817", "WAN-034315"],
 ["WAN-034972", "WAN-030741", "WAN-033682", "WAN-030882", "WAN-028898"],
 ["WAN-034972", "WAN-030741", "WAN-033468", "WAN-032405", "WAN-035266"],
 ["WAN-030741", "WAN-034958", "WAN-029188", "WAN-029558", "WAN-028898"],
 ["WAN-034972", "WAN-032114", "WAN-033468", "WAN-034958", "WAN-032597"],
 ["WAN-034660", "WAN-034972", "WAN-033468", "WAN-032405", "WAN-029114"],
 ["WAN-034972", "WAN-030741", "WAN-034958", "WAN-028898", "WAN-032597"],
 ["WAN-030741", "WAN-034633", "WAN-029558", "WAN-029114", "WAN-032597"],
 ["WAN-032114", "WAN-033682", "WAN-034958", "WAN-033529", "WAN-032776"],
 ["WAN-030741", "WAN-033468", "WAN-032776", "WAN-028898", "WAN-032597"],
 ["WAN-033682", "WAN-034958", "WAN-029188", "WAN-034633", "WAN-030817", "WAN-034315"],
 ["WAN-034972", "WAN-030741", "WAN-028940", "WAN-028898", "WAN-035266", "WAN-030817"],
 ["WAN-030741", "WAN-028940", "WAN-034958", "WAN-032776", "WAN-028898", "WAN-034315"],
 ["WAN-030741", "WAN-030882", "WAN-028898", "WAN-035266", "WAN-030817", "WAN-029114"],
 ["WAN-034972", "WAN-030882", "WAN-034958", "WAN-029558", "WAN-029114", "WAN-032597"],
 ["WAN-030741", "WAN-033682", "WAN-034958", "WAN-033529", "WAN-029372", "WAN-029558", "WAN-035266"],
 ["WAN-030882", "WAN-032405", "WAN-030817", "WAN-034315", "WAN-033210", "WAN-029114", "WAN-032597"],
 ["WAN-028940", "WAN-032405", "WAN-034958", "WAN-028898", "WAN-030817", "WAN-034315", "WAN-033210"],
 ["WAN-034660", "WAN-034972", "WAN-030741", "WAN-032114", "WAN-033468", "WAN-033682", "WAN-028940", "WAN-032405",
  "WAN-034958", "WAN-033529", "WAN-032776", "WAN-029372", "WAN-034633", "WAN-029558", "WAN-028898"]]
batch2 =batch
queue = []
open_orders = set()
update_open_orders = set
count_open_orders = 0
batch_amount_on_begin = len(batch)



def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def order_list_by_length(batch_list):
    return sorted(batch_list, key=len)


def add_queue_item(batch_list):
    for i in batch_list[0]:
        queue.append(i)


def delete_lu_from_lists(batch_list, item_to_delete):
    return [[item for item in sublist if item != item_to_delete] for sublist in batch_list]




orders_left = batch_amount_on_begin - len(batch)



while len(batch) > 0:
    # print(len(batch))
    print("queue: ", queue)
    print(len(queue), " LU left from shu")
    print(batch[0], "next lu to be add to the queue")
    # print(len(open_orders) - 140 + len(batch))
    print(len(open_orders), " opened orders at all")
    print(len(open_orders) - batch_amount_on_begin + len(batch), " opened orders left")
    print(len(open_orders) - batch_amount_on_begin + len(batch), " / ", len(batch), " opens orders")
    print(batch_amount_on_begin - len(batch), " orders completed")

    batch = order_list_by_length(batch)
    add_queue_item(batch)

    for i in batch[0]:
        update_open_orders = get_indicates_of_order_containing_lu(batch2, i)
        open_orders = open_orders.union(update_open_orders)
        batch = delete_lu_from_lists(batch, i)
    batch = [sublist for sublist in batch if sublist]  # remove empty lists

    # print(open_orders)
    print('!!!!!!!!!!!!!!!!!!!!!!')

if len(batch) == 0:
    print("queue: ", queue)
    print(len(queue), " LU left from shu")
    print("all orders are done")

# print(queue)

# petla sprawdzajaca  ktora wanna otworzy najmniej zlecen i ma najmniejsza ilosc wanien potrzebna do zamkniecia tych zlecen
# (suma wanien ktora musialaby wyjechac zeby zakonczyc zlecenia ktore rozpoeczela ta wanna)
# kazda wanne sprawdzamy czy nalezy do zbioru otwartych zlecen (+1pkt jezeli nie a -1pkt jezeli tak (mnoznik x2 jezezeli to jest ostatnia wanna z zamowienia (zamkne zlecenie))
# - wanna z najminejsza iloscia wyjezdza jako druga
# sprawdzamy w ktorych zleceniach byla ta wanna i  dodaje ja do listy do dalszego porownywaia z punktu poprzedniego
#

#

#
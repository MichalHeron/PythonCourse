# //enter file is a list of list of LU group by orders
#
# //function that as return gives ordered LU list


batch = [
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

queue = []
set_of_open_orders = set()
count_open_orders = 0
orders_amount_on_begin = len(batch)
point = 0
add_point_for_not_belong_to_order = 1
minus_point_for_belong_to_order = 3
minus_extra_point_for_last_lu_in_order = 5


def create_lu_list(batch):
    unique_set = set()
    for sublist in batch:
        unique_set.update(set(sublist))
    return unique_set


lu_list_set = create_lu_list(batch)
lu_set_length = len(lu_list_set)
lu_amount_on_begin = lu_set_length

def count_finished_orders():
    count = 0
    for i in batch:
        if len(i) < 1:
            count += 1
    return count


def get_lu_amount_of_order_containing_lu(main_list, target_value):
    return [len(sublist) for sublist in main_list if target_value in sublist]


def get_indicates_of_order_containing_lu(main_list, target_value):
    return set(index for index, sublist in enumerate(main_list) if target_value in sublist)


def delete_lu_from_lists(batch_list, item_to_delete):
    new_batch = []
    for sublist in batch_list:
        new_sublist = [item for item in sublist if item != item_to_delete]
        new_batch.append(new_sublist)
    return new_batch
    # return [sublist for sublist in batch_list if item_to_delete not in sublist]


def first_lu_in_queue(batch, lu_list_set):
    first_lu_points = 100000
    first_lu = "WAN-000000"
    for lu in lu_list_set:
        lu_points = sum(get_lu_amount_of_order_containing_lu(batch, lu))
        if lu_points < first_lu_points:
            first_lu_points = lu_points
            first_lu = lu
    return first_lu


def get_next_lu(): #generate next lu to queue - it searching LU which start the lowest amount of orders and which is part of started orders
    point = 10000
    lu_with_lowest_points = "WAN-000000"
    for lu in lu_list_set:
        new_point = 0
        order = 0
        for sublist in batch:
            if lu in sublist:
                if order not in set_of_open_orders:
                    new_point += add_point_for_not_belong_to_order
                if order in set_of_open_orders:
                    if len(sublist) < 2:
                        new_point -= minus_extra_point_for_last_lu_in_order
                        # print("extra minus point")
                    new_point -= minus_point_for_belong_to_order
            order += 1
        if new_point < point:
            point = new_point
            lu_with_lowest_points = lu
    return lu_with_lowest_points

set_of_open_orders = get_indicates_of_order_containing_lu(batch, first_lu_in_queue(batch, lu_list_set))
# set_of_open_orders = set_of_open_orders.union(get_indicates_of_order_containing_lu(batch, "WAN-033529"))

lu_amount_remaining =lu_set_length - 1


print("set of remaining LU: ", lu_list_set)
print(lu_set_length - 1, "LU lefts in queue")
print(23 - lu_amount_remaining, "LU left from shu")
print(len(batch), "orders waiting in queue (not finished yet)")

print(orders_amount_on_begin - len(batch), "finished orders")
queue.append(first_lu_in_queue(batch, lu_list_set))
print("first calculated LU: ", queue)
count_open_orders = len(set_of_open_orders)
print(count_open_orders, "open orders")
# print("set of open orders: ", set_of_open_orders)

batch = delete_lu_from_lists(batch, queue[-1])
lu_list_set.remove(queue[-1])

#########
while orders_amount_on_begin - count_finished_orders() > 0:
    print("NEXT LU @@@@@@@@@@@@@@@@@@@@@@@@")
    queue.append(get_next_lu())
    print("queue: ", queue)
    new_set_of_open_orders = get_indicates_of_order_containing_lu(batch, queue[-1])
    set_of_open_orders = set_of_open_orders.union(new_set_of_open_orders)
    # set_of_open_orders = get_indicates_of_order_containing_lu(batch, queue[-1])
    count_open_orders = len(set_of_open_orders)
    batch = delete_lu_from_lists(batch, queue[-1])
    if lu_list_set:
        lu_list_set.remove(queue[-1])
    else:
        lu_list_set.remove(0)
    lu_set_length = len(lu_list_set)
    empty_lists = [sublist for sublist in batch if len(sublist) == 0]
    print(lu_set_length, "LU lefts in queue")
    lu_amount_remaining = lu_set_length
    print(lu_amount_on_begin - lu_amount_remaining, "LU left from shu")

    print(orders_amount_on_begin - count_finished_orders(), "orders waiting in queue (not finished yet)")
    print(count_open_orders - len(empty_lists), " / ", orders_amount_on_begin - count_finished_orders(), " open orders")
    # print("set of open orders: ", set_of_open_orders)
    print(count_finished_orders(), " finished orders")


# print(get_lengths_of_lists_containing_value(batch, 'WAN-034972'))
#
# print(set(get_indices_of_lists_containing_value(batch, 'WAN-034972')))

# batch = [sublist for sublist in batch if sublist]  # remove empty lists

# petla sprawdzajaca  ktora wanna otworzy najmniej zlecen i ma najmniejsza ilosc wanien potrzebna do zamkniecia tych zlecen
# (suma wanien ktora musialaby wyjechac zeby zakonczyc zlecenia ktore rozpoeczela ta wanna)
# kazda wanne sprawdzamy czy nalezy do zbioru otwartych zlecen (+1pkt jezeli nie a -1pkt jezeli tak (mnoznik x2 jezezeli to jest ostatnia wanna z zamowienia (zamkne zlecenie))
# - wanna z najminejsza iloscia wyjezdza jako druga
# sprawdzamy w ktorych zleceniach byla ta wanna i  dodaje ja do listy do dalszego porownywaia z punktu poprzedniego
#

#

#


list_with_1m_elements = list(range(1_000_000))
set_with_1m_elements = set(list_with_1m_elements)

def find_1st_element_in_list():
    found = 0 in list_with_1m_elements
    assert found


def find_1st_element_in_set():
    found = 0 in set_with_1m_elements
    assert found

def find_last_element_in_list():
    found = 999_999 in list_with_1m_elements
    assert found


def find_last_element_in_set():
    found = 999_999 in set_with_1m_elements
    assert found


def find_lacking_element_in_list():
    found = -1 in list_with_1m_elements
    assert not found


def find_lacking_element_in_set():
    found = -1 in set_with_1m_elements
    assert not found


if __name__ == "__main__":
    find_1st_element_in_list()
    find_1st_element_in_set()
    find_last_element_in_list()
    find_last_element_in_set()
    find_lacking_element_in_list()
    find_lacking_element_in_set()

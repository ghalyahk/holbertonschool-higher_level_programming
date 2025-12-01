#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a new list with element replaced at index idx."""
    # إنشاء نسخة من القائمة الأصلية
    new_list = my_list.copy()
    
    # التحقق من صحة الفهرس
    if 0 <= idx < len(my_list):
        new_list[idx] = element

    return new_list

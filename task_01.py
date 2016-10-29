#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module combines two dictionaries on key value"""


def sum_orders(customers, orders):
    """This function combines customer and order dictionaries

    Args:
        customers (dic): customer information
        orders (dic): order information

    Returns:
        custumer_info (dic): key, name, email, count orders, total

    Example:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}>>>

    """

    customer_info = {}
    for key, value in customers.iteritems():
        num_orders = 0
        total_orders = 0
        for order in orders.values():
            if key == order['customer_id']:
                num_orders += 1
                total_orders += order['total']
                customer_info[key] = {'name': value['name'],
                                      'email': value['email'],
                                      'orders': num_orders,
                                      'total': total_orders}
    return customer_info

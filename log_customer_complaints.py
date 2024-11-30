import logging

logging.basicConfig(filename=r'D:\\Prog_file\\Project2\\env\\customer_complaints.log', level=logging.INFO)

def log_customer_complaint(customer_id, complaint):
    logging.info(f"Customer ID: {customer_id}, Complaint: {complaint}")


customer_complaints = [
    {'customer_id': 1, 'complaint': 'Unauthorized transaction on credit card'},
    {'customer_id': 2, 'complaint': 'Suspicious activity detected'},
    {'customer_id': 1, 'complaint': 'Unauthorized transaction on credit card'},
    {'customer_id': 2, 'complaint': 'Suspicious activity detected'},
    {'customer_id': 3, 'complaint': 'Order not received'},
    {'customer_id': 4, 'complaint': 'Incorrect billing'},
    {'customer_id': 5, 'complaint': 'Unable to login to account'}
]



for complaint in customer_complaints:
    log_customer_complaint(complaint['customer_id'], complaint['complaint'])

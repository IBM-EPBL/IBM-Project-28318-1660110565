o
    ��pc�  �                   @   sT   d dl Z d dlZd dlZd dlmZmZmZmZ dZ	e �
dd�Zdd� Zdd	� ZdS )
�    N)�Mail�Email�To�Contentzexpense tracker�smtp.gmail.com�K  c                 C   sN   t d� t�dd�}|��  |�dd� d�t| �}|�d||� |��  d S )Nz&sorry we cant process your candidaturer   r   �tproduct8080@gmail.comZlxixbmpnexbkiemhzSubject: {}

{}zil.tproduct8080@gmail.com)	�print�smtplib�SMTPZstarttls�login�format�SUBJECT�sendmail�quit)�TEXT�email�s�message� r   �~c:\Users\Smile\Documents\IBM-Project-5659-1658812620-main\Final Deliverables\Final Code\personal_expense_ttracker\sendemail.pyr      s   r   c           	      C   s^   t d�}t| �}d}td|�}t||||�}|�� }tjjjj	|d�}t
|j� t
|j� d S )Nr   zSending with SendGrid is Funz
text/plain)Zrequest_body)r   r   r   r   �get�sg�client�mail�send�postr	   �status_code�headers)	�userr   Z
from_emailZto_email�subject�contentr   Z	mail_json�responser   r   r   �sendgridmail   s   

r#   )r
   Zsendgridr   �osZsendgrid.helpers.mailr   r   r   r   r   r   r   r   r#   r   r   r   r   �<module>   s    

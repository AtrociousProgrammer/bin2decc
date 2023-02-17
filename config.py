import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'spiritually_enlightened_meerkat'

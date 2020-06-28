from locust import HttpUser, task, between
from random import sample
import faker


fake = faker.Faker()

existingWords = ['Goods', 'Department', 'nostrud']

class CommonUser(HttpUser):

    @task(1)
    def get_product_id(self):
        # self.client.get('/products/' + str(fake.random_int(3, 100000)), name='product_id')
        # self.client.get('/products/product?criteriaString=Goods', name='product_search_2')
        self.client.get('/search?q=' + fake.word(), name='product_non_existing_search')


    @task(10)
    def search(self):
        # self.client.get('/search?q=' + fake.word(), name='product_search')
        randomExistingWord = sample(existingWords, 1)[0]
        self.client.get('/products/product?criteriaString=' + randomExistingWord, name='product_existing_work_search')

    wait_time = between(5, 15)
# flask 프레임워크를 이용한, Restful API 서버 개발

from flask import Flask
from flask_restful import Api


from resources.recipe import RecipeListResource
from resources.recipe import RecipeResource
from resources.recipe import RecipePublishResource
# 기본 구조
app = Flask(__name__)

api = Api (app)

# APU 를 구분해서 실행시키는 것은,
# HTTP METHOD 와 URL 의 조합이다.

# 경로와 리소스(API코드)를 연결한다
api.add_resource( RecipeListResource , '/recipes')
api.add_resource( RecipeResource ,'/recipes/<int:recipe_id>')
api.add_resource( RecipePublishResource, '/recipes/<int:recipe_id>/publish')

if __name__ == '__main__':
    app.run()




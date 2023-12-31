<a name="readme-top"></a>



<!-- Значки -->
[![Участники][contributors-shield]][contributors-url]
[![Форки][forks-shield]][forks-url]
[![Звезды][stars-shield]][stars-url]
[![Проблемы][issues-shield]][issues-url]
[![Лицензия][license-shield]][license-url]



<!-- Титульник -->
<br />
<div align="center">
  <a href="https://github.com/LeonidAlekseev/djongo-blog">
    <img src="assets/logo.png" alt="Logo" height="80">
  </a>

  <h3 align="center">Djongo Blog</h3>

  <p align="center">
    Блог, основанный на Django с интеграцией Djongo для удобного использования MongoDB. Создавайте, управляйте и масштабируйте контент, благодаря высокой производительности и гибкости MongoDB.
    <br />
    <a href="https://github.com/LeonidAlekseev/djongo-blog"><strong>Изучить документацию »</strong></a>
    <br />
    <br />
    <a href="http://31.129.100.203:8080">Посмотреть демо</a>
    ·
    <a href="https://github.com/LeonidAlekseev/djongo-blog/issues">Сообщить о баге</a>
    ·
    <a href="https://github.com/LeonidAlekseev/djongo-blog/issues">Предложить изменение</a>
  </p>
</div>



<!-- Содержание -->
<details open>
  <summary>Содержание</summary>
  <ol>
    <li>
      <a href="#о-проекте">О проекте</a>
      <ul>
        <li><a href="#технологический-стек">Технологический стек</a></li>
      </ul>
    </li>
    <li>
      <a href="#начало-работы">Начало работы</a>
      <ul>
        <li><a href="#предварительные-требования">Предварительные требования</a></li>
        <li><a href="#установка">Установка</a></li>
      </ul>
    </li>
    <li><a href="#использование">Использование</a></li>
    <li><a href="#дорожная-карта">Дорожная карта</a></li>
    <li><a href="#содействие">Содействие</a></li>
    <li><a href="#лицензия">Лицензия</a></li>
    <li><a href="#контакты">Контакты</a></li>
    <li><a href="#источники">Источники</a></li>
  </ol>
</details>



<!-- О проекте -->
## О проекте

[![Product Name Screen Shot][product-screenshot]](http://31.129.100.203:8080)

Наш блог — это инновационная платформа, созданная на основе фреймворка Django с использованием Djongo для интеграции с MongoDB. Это не просто обычный блог: мы стремимся к созданию уникального пространства, где контент создается, управляется и отображается с невероятной легкостью и эффективностью. Используя преимущества Django вместе с гибкостью MongoDB, мы создали окружение, которое позволяет пользователям не только создавать контент, но и масштабировать его, обеспечивая уникальный опыт для каждого читателя.
<br />
<br />
Одной из наших ключевых целей было обеспечение максимальной гибкости и управления контентом. Djongo и MongoDB позволяют нам хранить данные в формате, который легко масштабировать и адаптировать под наши потребности. Это означает, что мы можем не только создавать и публиковать тексты, изображения и другие материалы, но и эффективно управлять структурой данных, что делает наш блог максимально гибким для изменений и дополнений.
<br />
<br />
Использование Djongo и MongoDB также дает нам преимущество в производительности. Благодаря высокой скорости работы MongoDB и эффективной интеграции с Django, мы можем обрабатывать большие объемы данных, обеспечивая быструю загрузку страниц и отзывчивость блога. Помимо этого, мы постоянно работаем над улучшением функционала блога, и наша конфигурация позволяет легко внедрять новые функции и развивать проект, чтобы соответствовать изменяющимся потребностям наших читателей и авторов контента.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Технологический стек

[![Docker][Docker.com]][Docker-url]
[![MongoDB][MongoDB.com]][MongoDB-url]
[![Python][Python.org]][Python-url]
[![Django][Django.com]][Django-url]
[![Javascript][Javascript.com]][Javascript-url]
[![JQuery][JQuery.com]][JQuery-url]
[![Bootstrap][Bootstrap.com]][Bootstrap-url]
[![PyTorch][PyTorch.com]][PyTorch-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Начало работы -->
## Начало работы

Чтобы запустить локальную копию, выполните следующие простые действия.

### Предварительные требования

Для запуска локальной копии необходимо установить Docker согласно [официальной инструкции](https://docs.docker.com/engine/install).
_Docker version 24.0.6 протестирован. Остерегайтесь более старых версий._

### Установка

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/LeonidAlekseev/djongo-blog.git
   ```
2. Настройте конфиги в папке `envs`
3. Используйте `Makefile` для сборки
    - Development
        - Build
        ```sh
        make dev
        ```
        - Up
        ```sh
        make up-dev
        ```
        - Down
        ```sh
        make down-dev
        ```
    - Production
        - Build
        ```sh
        make prod
        ```
        - Up
        ```sh
        make up-prod
        ```
        - Down
        ```sh
        make down-prod
        ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Использование -->
## Использование

Используйте это пространство для демонстрации полезных примеров использования проекта. В этом пространстве хорошо смотрятся дополнительные скриншоты, примеры кода и демо-версии. Вы также можете дать ссылку на дополнительные ресурсы.

_Дополнительные примеры приведены в разделе [Документация](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Дорожная карта -->
## Дорожная карта

- [x] Configs
    - [x] Environment Docker
    - [x] Environment MongoDB
    - [x] Environment Project
    - [x] Environment Nginx
- [x] Containers
    - [x] Docker MongoDB
    - [x] Docker Project
    - [x] Docker Nginx
    - [x] Docker Compose
- [x] Blog
    - [x] Home page
    - [x] Admin panel
    - [x] Pagination
    - [x] Translator
      - [x] Customization
    - [x] Authentication
        - [x] Permissions
        - [x] Groups
    - [x] Authorization
        - [x] Popup
    - [x] Registration
        - [x] Popup
    - [x] Search
    - [x] Profile
        - [x] Full Name
        - [x] Avatar
- [ ] Services
    - [x] CatBoost
        - [x] Process data
        - [x] Model training
        - [x] Building pipeline
        - [x] Integration
    - [ ] Spiking NN
        - [ ] Data processing
        - [ ] Model training
        - [ ] Building pipeline
        - [ ] Integration

Полный список предлагаемых возможностей и известных проблем в разделе [Открытые вопросы](https://github.com/LeonidAlekseev/djongo-blog/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Содействие -->
## Содействие

Содействие - это то, что делает сообщество разработчиков открытого кода таким удивительным местом для обучения, вдохновения и творчества. Любой ваш вклад будет **очень высоко оценен**.

Если у вас есть предложение, которое позволит сделать это лучше, пожалуйста, сделайте форк репозитория и создайте запрос на исправление. Вы также можете просто открыть проблему с тегом "улучшение".
Не забудьте поставить проекту звезду! Еще раз спасибо!

1. Сделайте форк проекта
2. Создайте свою ветку Feature
   ```sh
   git checkout -b feature/AmazingFeature
   ```
3. Зафиксируйте свои изменения
   ```sh
   git commit -m 'Add some AmazingFeature'
   ```
4. Переместите изменения в ветку
   ```sh
   git push origin feature/AmazingFeature
   ```
5. Откройте Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Лицензия -->
## Лицензия

Распространяется по лицензии Apache 2.0. Смотрите `LICENSE` для получения дополнительной информации.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Контакты -->
## Контакты

* Леонид - [@mister_lil](https://t.me/mister_lil)
* Александра - [@apoyka](https://t.me/apoyka)
* Кирилл - [@ontologic](https://t.me/ontologic)
* Антон - [@apossya](https://t.me/apossya)

Ссылка на проект: [https://github.com/LeonidAlekseev/djongo-blog](https://github.com/LeonidAlekseev/djongo-blog)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Источники -->
## Источники

* [Docker](https://docker.com)
* [Docker Compose](https://docs.docker.com/compose)
* [Makefile](https://wikipedia.org/wiki/Makefile)
* [MongoDB](https://mongodb.com)
* [Python](https://python.org)
* [Django](https://djangoproject.com)
* [Djongo](https://djongomapper.com)
* [Javascript](https://javascript.com)
* [JQuery](https://jquery.com)
* [Bootstrap](https://getbootstrap.com)
* [PyTorch](https://pytorch.org)
* [SNNTorch](https://snntorch.readthedocs.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Разметка -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/LeonidAlekseev/djongo-blog.svg?style=for-the-badge
[contributors-url]: https://github.com/LeonidAlekseev/djongo-blog/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LeonidAlekseev/djongo-blog.svg?style=for-the-badge
[forks-url]: https://github.com/LeonidAlekseev/djongo-blog/network/members
[stars-shield]: https://img.shields.io/github/stars/LeonidAlekseev/djongo-blog.svg?style=for-the-badge
[stars-url]: https://github.com/LeonidAlekseev/djongo-blog/stargazers
[issues-shield]: https://img.shields.io/github/issues/LeonidAlekseev/djongo-blog.svg?style=for-the-badge
[issues-url]: https://github.com/LeonidAlekseev/djongo-blog/issues
[license-shield]: https://img.shields.io/github/license/LeonidAlekseev/djongo-blog.svg?style=for-the-badge
[license-url]: https://github.com/LeonidAlekseev/djongo-blog/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: assets/screenshot.png
[Docker.com]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com
[MongoDB.com]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://mongodb.com
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org
[Django.com]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com
[Javascript.com]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[Javascript-url]: https://javascript.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[PyTorch.com]: https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[PyTorch-url]: https://pytorch.org
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com

# Анализ данных StackOverflow (SQL) 💾

## Описание таблиц базы данных

### Таблица `stackoverflow.badges` (значки)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор значка |
| `name` | str | Название значка (например, postgresql) |
| `user_id` | FK | ID пользователя (ссылка на `users.id`) |
| `creation_date` | date | Дата присвоения значка |

### Таблица `stackoverflow.post_types` (типы постов)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор типа поста |
| `type` | str | Тип: `Question` (вопрос) или `Answer` (ответ) |

### Таблица `stackoverflow.posts` (посты)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор поста |
| `title` | str | Заголовок поста |
| `creation_date` | date | Дата создания |
| `favorites_count` | int | Количество добавлений в закладки |
| `last_activity_date` | date | Дата последнего действия |
| `last_edit_date` | date | Дата последнего редактирования |
| `user_id` | FK | ID автора (ссылка на `users.id`) |
| `parent_id` | FK | ID родительского поста (для ответов) |
| `post_type_id` | FK | ID типа поста (ссылка на `post_types.id`) |
| `score` | int | Количество очков |
| `views_count` | int | Количество просмотров |

### Таблица `stackoverflow.users` (пользователи)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор пользователя |
| `creation_date` | date | Дата регистрации |
| `display_name` | str | Имя пользователя |
| `last_access_date` | date | Дата последнего входа |
| `location` | str | Местоположение |
| `reputation` | int | Очки репутации |
| `views` | int | Просмотры профиля |

### Таблица `stackoverflow.vote_types` (типы голосов)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор типа голоса |
| `name` | str | Тип: `UpMod` (полезный), `DownMod` (неполезный), `Close` (на доработку), `Offensive` (оскорбительный), `Spam` (реклама) |

### Таблица `stackoverflow.votes` (голоса)
| Поле | Тип | Описание |
|------|-----|----------|
| `id` | PK | Идентификатор голоса |
| `post_id` | FK | ID поста (ссылка на `posts.id`) |
| `user_id` | FK | ID голосующего (ссылка на `users.id`) |
| `bounty_amount` | int | Сумма вознаграждения |
| `vote_type_id` | FK | ID типа голоса (ссылка на `vote_types.id`) |
| `creation_date` | date | Дата голосования |

**Обозначения**:
- PK — Primary Key (первичный ключ)
- FK — Foreign Key (внешний ключ)
import logging

import pandas as pd
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s"
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)

APP_TOKEN = "SECRET_TOKEN"
PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"

bot = Bot(token=APP_TOKEN)
dp = Dispatcher(bot)

def get_todo_data():
    return pd.read_csv(PATH_TO_TODO_TABLE)

@dp.message_handler(commands="all")
async def all_tasks(payload: types.Message):
    await payload.reply(f"```{get_todo_data().to_markdown()}```", parce_mode = "Markdown")

@dp.message_handler(commands="add")
async def add_task(payload: types.Message):
    text = payload.get_args().strip()
    new_task = pd.DataFrame({"text":[text], "status":["active"]})
    updated_tasks = pd.concat([get_todo_data(), new_task], ignore_index=True, axis=0)

    updated_tasks.to_csv(PATH_TO_TODO_TABLE, index=False)

    logging.info(f"Добавил в таблицу задачу - {text}")
    await payload.reply(f"Добавил задачу: *{text}*", parse_mode="markdown")

@dp.message_handler(commands="done")
async def complete_task(payload: types.Message):
    text = payload.get_args().stirp()
    df = get_todo_data()
    df.loc[df.text == text, "status"] = "complete"

    df.to_csv(PATH_TO_TODO_TABLE, index=False)

    logging.info(f"Выполнил задачу - {text}")
    await payload.reply(f"Выполнено : *{text}*", parse_mode="Markdown")

if __name__ == 'main':
    executor.start_polling(dp)
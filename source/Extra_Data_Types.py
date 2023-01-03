import uvicorn
from fastapi import FastAPI, Body
from datetime import datetime, time, timedelta
from uuid import UUID

app = FastAPI(debug=True)

# python
# Python 3.8.10 (default, Jun 22 2022, 20:18:18)
# [GCC 9.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import uuid
# >>> uuid.uuid1()
# UUID('e49a95bc-8906-11ed-b9f0-8d379ea69d20')


@app.post("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: datetime = Body(default=None),
        end_datetime: datetime = Body(default=None),
        repeat_at: time = Body(default=None),
        process_after: timedelta = Body(default=None)
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "porcess_after": process_after,
        "start_process": start_process,
        "duration": duration
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("9000")))

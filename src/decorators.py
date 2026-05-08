from typing import Callable, TypeVar, Any, Optional
import functools

R = TypeVar("R")  # Обобщенный тип для возвращаемого значения декорируемой функции


def log(filename: Optional[str] = None) -> Callable[[Callable[..., R]], Callable[..., R]]:
    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise
            else:
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
            return result

        return wrapper

    return decorator

import gc
import os
from dataclasses import dataclass
from logging import Logger
from time import time
from typing import Any, Optional

import psutil


@dataclass
class Memory:
    memory_full_info: Any
    virtual_memory: Any
    swap_memory: Any

    @staticmethod
    def snapshot():
        proc = psutil.Process(os.getpid())
        return Memory(
            proc.memory_full_info(),
            psutil.virtual_memory(),
            psutil.swap_memory(),
        )


@dataclass
class Gc:
    pre: Memory
    post: Memory
    elapsed: float

    @staticmethod
    def snapshot(logger: Optional[Logger] = None) -> 'Gc':
        pre = Memory.snapshot()
        start = time()
        gc.collect()
        elapsed = time() - start
        post = Memory.snapshot()

        if logger:
            logger.debug(f"gc:  pre={pre}")
            logger.debug(f"gc: post={post}")

        return Gc(pre=pre, post=post, elapsed=elapsed)

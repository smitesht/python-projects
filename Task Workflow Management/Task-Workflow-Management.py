from dataclasses import dataclass, field
from typing import List, Protocol, Optional
from datetime import datetime, timedelta

# Define TaskState abstraction with the Protocol
class TaskState(Protocol):
    def handle(self, context: "TaskContext") -> None:
        pass

    def current_state(self) -> str:
        pass

# Define TaskObserver abstraction with the Protocol
class TaskObserver(Protocol):
    def update(self, message: str) -> None:
        pass

# Handle TaskObservers and implement notification
@dataclass
class TaskContext:
    state: TaskState
    observers: List[TaskObserver] = field(default_factory=list)

    # change task state
    def set_state(self, state: TaskState) -> None:
        self.state = state
        
    def add_observer(self, observer: TaskObserver) -> None:
        self.observers.append(observer)

    # notify all the TaskObservers like Email and SMS
    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)

    def execute_state(self) -> None:
        self.state.handle(self)

    @property
    def current_state(self) -> str:
        return self.state.current_state()

# Implement TaskState
class CreateState:
    def handle(self, context: TaskContext) -> None:
        message = "Task has been created."
        print(message)
        context.notify_observers(message)

    def current_state(self) -> str:
        return "Created"

# Implement TaskState
class InProgressState:
    def handle(self, context: TaskContext) -> None:
        message = "Task is now In Progress."
        print(message)
        context.notify_observers(message)

    def current_state(self) -> str:
        return "In Progress"

# Implement TaskState
class CompletedState:
    def handle(self, context: TaskContext) -> None:
        message = "Task has been completed."
        print(message)
        context.notify_observers(message)

    def current_state(self) -> str:
        return "Completed"

# Implement TaskState
class CancelledState:
    def handle(self, context: TaskContext) -> None:
        message = "Task has been cancelled."
        print(message)
        context.notify_observers(message)

    def current_state(self) -> str:
        return "Cancelled"

# Implement TaskObserver
class EmailTaskObserver:
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str) -> None:
        print(f"Email sent to {self.email}: {message}")

# Implement TaskObserver
class SMSTaskObserver:
    def __init__(self, phone: str):
        self.phone = phone

    def update(self, message: str) -> None:
        print(f"SMS sent to {self.phone}: {message}")

# Implement Task
@dataclass
class Task:
    id: int
    title: str
    priority: str
    description: Optional[str] = ""
    start_date: datetime = field(default_factory=lambda: datetime.now())
    end_date: datetime = field(default_factory=lambda: datetime.now() + timedelta(days=2))
    context: TaskContext = field(default_factory=lambda: TaskContext(CreateState()))

    def add_observer(self, observer: TaskObserver) -> None:
        self.context.add_observer(observer)

    def change_state(self, state: TaskState) -> None:
        self.context.set_state(state)
        self.context.execute_state()

    @property
    def current_state(self) -> str:
        return self.context.current_state

    def __str__(self) -> str:
        return (f"Task Details\n"
                f"ID: {self.id}, Priority: {self.priority}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}, End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
                f"Current State: {self.current_state}")

# Usage
if __name__ == "__main__":
    task = Task(id=1001, title="Python Dev Task", priority="Low")
    task.add_observer(EmailTaskObserver("john.test@gmail.com"))
    task.add_observer(EmailTaskObserver("martha.test@gmail.com"))
    task.add_observer(SMSTaskObserver("+1-234-567-890"))

    print(task)
    print()

    task.change_state(InProgressState())
    print()

    task.change_state(CompletedState())
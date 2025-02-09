function editTask(taskId) {
    const taskItem = document.querySelector(`.task-item[data-id="${taskId}"]`);
    const title = taskItem.querySelector('h3').innerText;
    const description = taskItem.querySelector('p').innerText;
    const dueDate = taskItem.querySelector('p:nth-child(3)').innerText.replace('期限: ', '');
    const tags = taskItem.querySelector('p:nth-child(4)').innerText.replace('タグ: ', '');

    const newTitle = prompt("タスク名を編集", title);
    const newDescription = prompt("説明を編集", description);
    const newDueDate = prompt("期限を編集", dueDate);
    const newTags = prompt("タグを編集 (カンマ区切り)", tags);

    if (newTitle !== null) {
        fetch(`/edit/${taskId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // JSON として送信
            },
            body: JSON.stringify({
                title: newTitle,
                description: newDescription,
                due_date: newDueDate,
                tags: newTags
            })
        }).then(() => window.location.reload());
    }
}

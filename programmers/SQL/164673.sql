-- 코드를 입력하세요
SELECT TITLE, USED_GOODS_BOARD.BOARD_ID, REPLY_ID, USED_GOODS_REPLY.WRITER_ID, USED_GOODS_REPLY.CONTENTS, TO_CHAR(USED_GOODS_REPLY.CREATED_DATE, 'YYYY-MM-DD') AS CREATE_DATE
FROM USED_GOODS_BOARD
RIGHT JOIN USED_GOODS_REPLY ON USED_GOODS_REPLY.BOARD_ID = USED_GOODS_BOARD.BOARD_ID
WHERE TO_CHAR(USED_GOODS_BOARD.CREATED_DATE, 'YYYY-MM') = '2022-10'
ORDER BY USED_GOODS_REPLY.CREATED_DATE ASC, TITLE ASC;
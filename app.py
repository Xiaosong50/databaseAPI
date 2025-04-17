from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'Lxs,123321',
    'database': 'student_survay',
    'charset': 'utf8mb4'
}



@app.route('/skills', methods=['POST'])
def save_skills_response():
    data = request.json

    student_id = data.get("student_id")
    java_response = data.get("java_response")
    sql_response = data.get("sql_response")
    data_mining_response = data.get("data_mining_response")
    IOT_response = data.get("IOT_response")
    HCI_response = data.get("HCI_response")
    blockchains_response = data.get("blockchains_response")

    # 必填校验（仅学生ID，其他字段允许为空）
    if not all([student_id, java_response, sql_response, data_mining_response, IOT_response, HCI_response, blockchains_response]):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO llm_response_skills (
                    student_id,
                    java_response,
                    sql_response,
                    data_mining_response,
                    IOT_response,
                    HCI_response,
                    blockchains_response
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                student_id,
                java_response,
                sql_response,
                data_mining_response,
                IOT_response,
                HCI_response,
                blockchains_response
            ))
        conn.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500



# hobbies

@app.route('/hobbies', methods=['POST'])
def save_hobbies_response():
    data = request.json

    student_id = data.get("student_id")
    java_response = data.get("java_response")
    sql_response = data.get("sql_response")
    data_mining_response = data.get("data_mining_response")
    IOT_response = data.get("IOT_response")
    HCI_response = data.get("HCI_response")
    blockchains_response = data.get("blockchains_response")

    # 必填校验（仅学生ID，其他字段允许为空）
    if not all([student_id, java_response, sql_response, data_mining_response, IOT_response, HCI_response, blockchains_response]):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO llm_response_hobbies (
                    student_id,
                    java_response,
                    sql_response,
                    data_mining_response,
                    IOT_response,
                    HCI_response,
                    blockchains_response
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                student_id,
                java_response,
                sql_response,
                data_mining_response,
                IOT_response,
                HCI_response,
                blockchains_response
            ))
        conn.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# subjects

@app.route('/subjects', methods=['POST'])
def save_subjects_response():
    data = request.json

    student_id = data.get("student_id")
    java_response = data.get("java_response")
    sql_response = data.get("sql_response")
    data_mining_response = data.get("data_mining_response")
    IOT_response = data.get("IOT_response")
    HCI_response = data.get("HCI_response")
    blockchains_response = data.get("blockchains_response")

    # 必填校验（仅学生ID，其他字段允许为空）
    if not all([student_id, java_response, sql_response, data_mining_response, IOT_response, HCI_response, blockchains_response]):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO llm_response_subjects (
                    student_id,
                    java_response,
                    sql_response,
                    data_mining_response,
                    IOT_response,
                    HCI_response,
                    blockchains_response
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                student_id,
                java_response,
                sql_response,
                data_mining_response,
                IOT_response,
                HCI_response,
                blockchains_response
            ))
        conn.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# default
@app.route('/default', methods=['POST'])
def save_default_response():
    data = request.json

    response_type = data.get("response_type")
    response = data.get("response")
    

    # 必填校验（仅学生ID，其他字段允许为空）
    if not all([response_type, response]):
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO llm_response_default (
                    response_type,
                    response
                ) VALUES (%s, %s)
            """
            cursor.execute(sql, (
                response_type,
                response
            ))
        conn.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        //static string strConn = "Server=210.125.198.245;Database=202118003_kgj;Uid=study;Pwd=1q2w3e4r;";
        //MySqlConnection conn = new MySqlConnection(strConn);

        public Form1()
        {
            InitializeComponent();
        }

        // 데이터 조회 버튼 이벤트
        private void button1_Click(object sender, EventArgs e)
        {
            string connStr = "Server=210.125.198.245;Database=202118003_kgj;Uid=study;Pwd=1q2w3e4r;";

            using (MySqlConnection conn = new MySqlConnection(connStr))
            {
                try
                {
                    conn.Open();
                    //string sql = "SELECT * FROM account WHERE id";
                    string sql = "select pw from account where name = '" + this.textBox1.Text + "';";

                    //ExecuteReader를 이용하여
                    //연결 모드로 데이타 가져오기
                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    MySqlDataReader rdr = cmd.ExecuteReader();
                    while (rdr.Read())
                    {
                        this.textBox2.Text = string.Format("{0}", rdr["pw"]);
                        //MessageBox.Show(string.Format("name: {0}", rdr["name"]));
                        //MessageBox.Show(string.Format("id: {0}, name: {1}, pw: {2}, staff_id: {3}", rdr["id"], rdr["name"], rdr["pw"], rdr["staff_id"]));
                        //Console.WriteLine("{0}: {1}", rdr["id"], rdr["name"]);
                    }
                    rdr.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // 데이터 수정 버튼 이벤트
        private void button2_Click(object sender, EventArgs e)
        {
            string connStr = "Server=210.125.198.245;Database=202118003_kgj;Uid=study;Pwd=1q2w3e4r;";

            using (MySqlConnection conn = new MySqlConnection(connStr))
            {
                try
                {
                    conn.Open();
                    string sql = "update account set name = '" + this.textBox1.Text + "' where id = '" + this.textBox3.Text + "';";

                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    MySqlDataReader rdr = cmd.ExecuteReader();
                    while (rdr.Read())
                    {
                    }
                    MessageBox.Show("수정 완료");
                    rdr.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // 데이터 삭제 버튼 이벤트
        private void button3_Click(object sender, EventArgs e)
        {
            string connStr = "Server=210.125.198.245;Database=202118003_kgj;Uid=study;Pwd=1q2w3e4r;";

            using (MySqlConnection conn = new MySqlConnection(connStr))
            {
                try
                {
                    conn.Open();
                    string sql = "delete from account where name = '" + this.textBox1.Text + "' and id = '" + this.textBox3.Text + "';";

                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    MySqlDataReader rdr = cmd.ExecuteReader();
                    while (rdr.Read())
                    {
                    }
                    MessageBox.Show("삭제 완료");
                    rdr.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // 데이터 추가 버튼 이벤트
        private void button4_Click(object sender, EventArgs e)
        {
            string connStr = "Server=210.125.198.245;Database=202118003_kgj;Uid=study;Pwd=1q2w3e4r;";
            string sql = "insert into account (id, name, pw, staff_id) " + "values" +
            "('" + this.textBox3.Text + "', '" + this.textBox1.Text +
            "', '" + this.textBox4.Text + "', '" + this.textBox5.Text + "');";

            using (MySqlConnection conn = new MySqlConnection(connStr))
            {
                try
                {
                    conn.Open();

                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    MySqlDataReader rdr = cmd.ExecuteReader();
                    MessageBox.Show("추가 완료");
                    while (rdr.Read())
                    {
                    }
                    conn.Close();
                    rdr.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // 폼 이동
        private Point mousePoint;

        private void panel3_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                int x = mousePoint.X - e.X;
                int y = mousePoint.Y - e.Y;
                Location = new Point(this.Left - x, this.Top - y);
            }
        }

        private void panel3_MouseDown(object sender, MouseEventArgs e)
        {
            mousePoint = new Point(e.X, e.Y); // 지금 윈도우의 좌표 저장
        }

        // 폼 종료
        private void label5_Click(object sender, EventArgs e)
        {
            Application.OpenForms["Form1"].Close();
        }
    }
}

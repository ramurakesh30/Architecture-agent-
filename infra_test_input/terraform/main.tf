resource "aws_instance" "web" {

  ami = "ami-123456"

  instance_type = "t3.micro"

  associate_public_ip_address = true

  tags = {
    Name = "web-server"
  }
}
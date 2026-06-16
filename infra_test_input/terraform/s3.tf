resource "aws_s3_bucket" "uploads" {

  bucket = "company-uploads"

  acl = "public-read"
}

resource "aws_iam_policy" "admin" {

  policy = jsonencode({

    Statement = [

      {
        Effect = "Allow"

        Action = "*"

        Resource = "*"
      }
    ]
  })
}

password = "supersecret123"
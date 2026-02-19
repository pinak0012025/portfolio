variable "project_id" {
  description = "The GCP Project ID"
  type        = string
}

variable "region" {
  default = "us-central1"
  type    = string
}

variable "zone" {
  default = "us-central1-a"
  type    = string
}

variable "machine_type" {
  default     = "e2-medium"
  description = "VM size for Jenkins"
  type        = string
}
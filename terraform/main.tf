# Artifact Registry for Docker images
resource "google_artifact_registry_repository" "docker_repo" {
  location      = var.region
  repository_id = "commercial-app-repo"
  format        = "DOCKER"
}

# Network Firewall for Jenkins access
resource "google_compute_firewall" "jenkins_fw" {
  name    = "jenkins-allow-8080"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["8080", "22"]
  }
  source_ranges = ["0.0.0.0/0"]
}

# Jenkins VM Instance
resource "google_compute_instance" "jenkins_vm" {
  name         = "jenkins-server"
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 50
    }
  }

  network_interface {
    network = "default"
    access_config {} # Assigns ephemeral Public IP
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y docker.io openjdk-11-jdk
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update && sudo apt-get install -y jenkins
    sudo usermod -aG docker jenkins
    sudo systemctl restart jenkins
  EOT
}
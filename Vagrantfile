ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
Vagrant.configure("2") do |config|
 config.vm.boot_timeout=600
 config.vm.define "flask-app" do |a|
    a.vm.provider "docker" do |d|
        d.image="rofrano/vagrant-provider:ubuntu"
        d.ports=["5000:5000"]
        d.name = "flask-app"
        d.privileged="false"
        d.has_ssh="true"
    end
 end
end
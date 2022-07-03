require 'mina/multistage'
require 'mina/deploy'
require 'mina/git'

set :application_name, 'search-engines-scraper'
set :repository, 'git@github.com:encoreshao/search-engines-scraper.git'
set :shared_dirs, fetch(:shared_dirs, []).push('pids', 'sockets', 'log', 'public')
set :forward_agent, true
set :stages, %w(production)

set :user, ENV['SSH_USER'] || `whoami`.chop
set :deploy_to, "/var/www/#{fetch(:env)}/#{fetch(:application_name)}"
set :pyenv_venv, "#{fetch(:application_name)}"
set :monit_group, "#{fetch(:application_name)}"

desc "Deployment..."
task deploy: :remote_environment do
  deploy do
    invoke :'git:clone'
    invoke :'deploy:link_shared_paths'

    on :launch do
      in_path(fetch(:current_path)) do
        comment "Installing requirements"
        command %{source /etc/profile.d/pyenv.sh}
        command %{pyenv activate #{fetch(:pyenv_venv)}}
        command %{python3 setup.py install}
      end
    end

    invoke :'deploy:cleanup'
  end
end

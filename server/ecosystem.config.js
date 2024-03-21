module.exports = {
  apps : [{
    name: 'circlism',
    script: 'run.py',
	interpreter: './env/bin/python3',
	interpreter_arg: './env/bin/python3',
    // Options reference: https://pm2.keymetrics.io/docs/usage/application-declaration/
    args: '',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      PORT: 5000,
      NODE_ENV: 'development'
    },
    env_production: {
      PORT: 5000,
      NODE_ENV: 'production'
    }
  }],
};
